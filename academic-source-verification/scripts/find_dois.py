#!/usr/bin/env python3
"""
find_dois.py — companion to check_dois.py.

For every DOI in references.bib that is DEAD (does not resolve) or points to the
WRONG article, this searches CrossRef by the bib title + first author and proposes
the correct DOI. If no confident candidate is found, it flags "REVIEW / maybe REMOVE"
(some older articles genuinely have no DOI — better no field than a dead link).

READ-ONLY: never edits references.bib. Writes DOI_FIX_PROPOSALS.md.

Run on a machine with internet, from the project root:
    python3 00_meta/translation/find_dois.py references.bib
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
UA     = {"User-Agent": f"DOIfix/1.0 (mailto:{MAILTO})"}

def norm(s):
    s = re.sub(r'\{|\}|\\[a-zA-Z]+', '', s)
    return re.sub(r'[^a-z0-9 ]', '', re.sub(r'\s+', ' ', s.lower())).strip()
def sim(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
        return json.load(r)

text = open(BIB, encoding="utf-8").read()
recs = []
for e in re.split(r'(?=@\w+\{)', text):
    km = re.match(r'@\w+\{([^,]+),', e)
    if not km:
        continue
    def fld(n):
        m = re.search(n + r'\s*=\s*[{"](.+?)[}"]\s*,?\s*$', e, re.I | re.M)
        return m.group(1).strip() if m else ""
    recs.append((km.group(1).strip(), fld("title"), fld("author"), fld("year"), fld("doi")))

def resolve(doi, title):
    try:
        msg = get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="") + f"?mailto={MAILTO}").get("message", {})
        ct = (msg.get("title") or [""])[0]
        return True, ct, (sim(title, ct) if title else 1.0)
    except urllib.error.HTTPError as ex:
        return False, f"HTTP {ex.code}", 0.0
    except Exception as ex:
        return False, "ERR:" + type(ex).__name__, 0.0

props = []
for key, title, author, year, doi in recs:
    if not doi:
        continue
    ok, ct, ratio = resolve(doi, title)
    if ok and ratio > 0.75:
        time.sleep(0.25)
        continue  # clean
    reason = "dead — does not resolve (%s)" % ct if not ok else "points to '%s' (%.2f)" % (ct[:55], ratio)
    a1 = re.split(r'\s+and\s+', author)[0].split(",")[0].strip() if author else ""
    q = "https://api.crossref.org/works?rows=3&select=DOI,title,published&query.bibliographic=" + urllib.parse.quote(title)
    if a1:
        q += "&query.author=" + urllib.parse.quote(a1)
    q += f"&mailto={MAILTO}"
    cands = []
    try:
        for it in get(q).get("message", {}).get("items", []):
            ct2 = (it.get("title") or [""])[0]
            cands.append((it.get("DOI", ""), ct2, sim(title, ct2)))
    except Exception as ex:
        cands = [("", "(search error: %s)" % type(ex).__name__, 0.0)]
    cands.sort(key=lambda x: -x[2])
    best = cands[0] if cands else ("", "", 0.0)
    rec = "REPLACE with %s" % best[0] if best[2] > 0.85 else "REVIEW / maybe REMOVE (no confident match — may have no DOI)"
    props.append((key, title, doi, reason, cands, rec))
    print(f"{key}: {rec}")
    time.sleep(0.4)

with open("DOI_FIX_PROPOSALS.md", "w", encoding="utf-8") as f:
    f.write("# DOI fix proposals (CrossRef title search)\n\n")
    f.write(f"{len(props)} entries with a bad DOI. For each: the current (bad) DOI, why it's flagged, "
            f"and the best CrossRef candidate(s). Nothing is changed automatically.\n\n")
    for key, title, doi, reason, cands, rec in props:
        f.write(f"## {key}\n")
        f.write(f"- bib title : {title}\n")
        f.write(f"- current DOI : `{doi}`  — {reason}\n")
        f.write(f"- **recommendation : {rec}**\n")
        f.write(f"- candidates :\n")
        for d, ct, r in cands:
            f.write(f"    - `{d}`  ({r:.2f})  {ct[:75]}\n")
        f.write("\n")
print(f"\nWrote DOI_FIX_PROPOSALS.md ({len(props)} entries)")
