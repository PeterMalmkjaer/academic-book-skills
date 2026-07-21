#!/usr/bin/env python3
"""
check_dois.py — resolution + title-match check for EVERY DOI in references.bib.

Queries the CrossRef REST API for each DOI and compares the returned article
title to the title in references.bib, so you catch (a) DOIs that do not resolve
and (b) DOIs that resolve to a DIFFERENT article than cited.

READ-ONLY: never edits references.bib. Writes a report to DOI_CHECK_REPORT.md.

Run on a machine with internet (e.g. your Mac), from the project root:
    python3 00_meta/translation/check_dois.py references.bib

Notes:
- Uses CrossRef's "polite pool" via a mailto in the User-Agent — please keep it.
- ~135 requests at 0.3s spacing ≈ under a minute.
"""
import os
import re, sys, json, time, urllib.parse, urllib.request, urllib.error, difflib

BIB    = sys.argv[1] if len(sys.argv) > 1 else "references.bib"
MAILTO = os.environ.get("CROSSREF_MAILTO", "").strip()
if not MAILTO:
    sys.exit("Set CROSSREF_MAILTO to your own e-mail address before running.\n"
             "CrossRef's polite pool identifies the caller, so it must be YOUR address,\n"
             "not the author's — CrossRef contacts it about traffic from your machine.\n"
             "  export CROSSREF_MAILTO='you@example.org'")

def norm(s):
    s = re.sub(r'\{|\}|\\[a-zA-Z]+', '', s)          # strip LaTeX
    return re.sub(r'[^a-z0-9 ]', '', re.sub(r'\s+', ' ', s.lower())).strip()

text = open(BIB, encoding="utf-8").read()
entries = re.split(r'(?=@\w+\{)', text)
rows = []
for e in entries:
    km = re.match(r'@\w+\{([^,]+),', e)
    if not km:
        continue
    dm = re.search(r'doi\s*=\s*[{"]([^}"]+)', e, re.I)
    tm = re.search(r'title\s*=\s*[{"](.+?)[}"]\s*,?\s*$', e, re.I | re.M)
    if dm:
        rows.append((km.group(1).strip(), dm.group(1).strip(), tm.group(1).strip() if tm else ""))

print(f"Checking {len(rows)} DOIs via CrossRef ...\n")
out = []
for i, (key, doi, title) in enumerate(rows, 1):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="") + f"?mailto={MAILTO}"
    status, cr_title, verdict = "?", "", ""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": f"DOIcheck/1.0 (mailto:{MAILTO})"})
        with urllib.request.urlopen(req, timeout=25) as r:
            msg = json.load(r).get("message", {})
            status = "200"
            cr_title = (msg.get("title") or [""])[0]
    except urllib.error.HTTPError as ex:
        status = str(ex.code)
    except Exception as ex:
        status = "ERR:" + type(ex).__name__

    if status == "200":
        if not title:
            verdict = "RESOLVES (no bib title)"
        else:
            ratio = difflib.SequenceMatcher(None, norm(title), norm(cr_title)).ratio()
            verdict = "MATCH" if ratio > 0.75 else f"MISMATCH ({ratio:.2f})"
    elif status == "404":
        verdict = "NOT FOUND — does not resolve"
    else:
        verdict = f"CHECK ({status})"
    out.append((key, doi, status, verdict, cr_title, title))
    print(f"[{i:3}/{len(rows)}] {key:32} {verdict}")
    time.sleep(0.3)

bad = [r for r in out if not (r[3].startswith("MATCH") or r[3].startswith("RESOLVES"))]
with open("DOI_CHECK_REPORT.md", "w", encoding="utf-8") as f:
    f.write("# DOI check report (CrossRef)\n\n")
    f.write(f"- Total DOIs: {len(out)}\n- Clean (MATCH / RESOLVES): {len(out)-len(bad)}\n- **To review: {len(bad)}**\n\n")
    f.write("## Needs review\n\n| key | doi | status | verdict | CrossRef title | bib title |\n|---|---|---|---|---|---|\n")
    for key, doi, st, vd, ct, bt in bad:
        f.write(f"| {key} | `{doi}` | {st} | {vd} | {ct[:70]} | {bt[:70]} |\n")
    f.write("\n## All DOIs\n\n| key | doi | status | verdict |\n|---|---|---|---|\n")
    for key, doi, st, vd, ct, bt in out:
        f.write(f"| {key} | `{doi}` | {st} | {vd} |\n")

print(f"\nDone. {len(out)-len(bad)}/{len(out)} clean, {len(bad)} to review.")
print("Report: DOI_CHECK_REPORT.md")
