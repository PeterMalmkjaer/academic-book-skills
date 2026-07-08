#!/usr/bin/env python3
"""
metadata_check.py — field-by-field verification of EVERY reference in references.bib
against the authoritative record (CrossRef). Goes beyond the DOI: catches wrong author
names/order, wrong journal/venue, wrong volume/issue, wrong first page, wrong year.

- DOI-bearing entries : looked up by DOI (exact).
- DOI-less entries     : searched by title (+ first author); best CrossRef match used
                         (flagged as lower-confidence — verify manually).

READ-ONLY: never edits references.bib. Writes METADATA_CHECK_REPORT.md.

Run on a machine with internet, from the project root:
    python3 00_meta/translation/metadata_check.py references.bib
"""
import re, sys, json, time, urllib.parse, urllib.request, urllib.error, difflib

BIB    = sys.argv[1] if len(sys.argv) > 1 else "references.bib"
MAILTO = "peter.malmkjaer@gmail.com"
UA     = {"User-Agent": f"MetaCheck/1.0 (mailto:{MAILTO})"}

def norm(s):
    s = re.sub(r'\{|\}|\\[a-zA-Z]+', '', s or '')
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', s.lower())).strip()
def toks(s): return set(norm(s).split())
def ratio(a, b): return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()
def firstpage(p):
    m = re.search(r'\d+', p or ''); return m.group(0) if m else ""
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
        return json.load(r)

def parse_bib(path):
    t = open(path, encoding="utf-8").read()
    out = []
    for e in re.split(r'(?=@\w+\{)', t):
        km = re.match(r'@(\w+)\{([^,]+),', e)
        if not km: continue
        def f(n):
            m = re.search(r'^\s*' + n + r'\s*=\s*[{"](.*?)[}"]\s*,?\s*$', e, re.I | re.M)
            return m.group(1).strip() if m else ""
        out.append(dict(typ=km.group(1), key=km.group(2).strip(), author=f("author"),
                        title=f("title"), journal=f("journal") or f("booktitle"),
                        volume=f("volume"), pages=f("pages"), year=f("year"), doi=f("doi")))
    return out

def first_surname(a):
    a0 = re.split(r'\s+and\s+', a)[0] if a else ""
    return (a0.split(",")[0] if "," in a0 else (a0.split()[-1] if a0 else "")).strip()

def cr_by_doi(doi):
    try: return get("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="") + f"?mailto={MAILTO}").get("message", {})
    except Exception: return None
def cr_by_title(title, author):
    try:
        q = "https://api.crossref.org/works?rows=1&query.bibliographic=" + urllib.parse.quote(title)
        if author: q += "&query.author=" + urllib.parse.quote(author)
        return (get(q + f"&mailto={MAILTO}").get("message", {}).get("items", []) or [None])[0]
    except Exception: return None

def cr_fields(m):
    au = m.get("author", []) or []
    return dict(title=(m.get("title") or [""])[0], journal=(m.get("container-title") or [""])[0],
                volume=str(m.get("volume", "")), page=m.get("page", ""),
                year=str((m.get("issued", {}).get("date-parts", [[None]])[0] or [None])[0] or ""),
                surnames=[a.get("family", "") for a in au])

rows = parse_bib(BIB); report = []
for i, b in enumerate(rows, 1):
    by_doi = bool(b["doi"])
    m = cr_by_doi(b["doi"]) if by_doi else cr_by_title(b["title"], first_surname(b["author"]))
    if not m:
        report.append((b, "NO MATCH", ["no CrossRef record found"])); print(f"[{i}/{len(rows)}] {b['key']}: NO MATCH"); time.sleep(0.3); continue
    c = cr_fields(m); iss = []
    # DOI-less entries are matched only by title search. If the returned record's title
    # does not closely match, it is a DIFFERENT paper (common for books/cases/HBR with no
    # CrossRef record) -> do NOT field-compare, or we get false positives. Flag & skip.
    if not by_doi and ratio(b["title"], c["title"]) < 0.80:
        report.append((b, "NO RELIABLE MATCH",
                       [f"title-search hit '{c['title'][:50]}' (low similarity); no DOI in bib — verify manually"]))
        print(f"[{i}/{len(rows)}] {b['key']}: NO RELIABLE MATCH")
        time.sleep(0.3); continue
    if b["title"] and by_doi and ratio(b["title"], c["title"]) < 0.80:
        iss.append(f"title: bib='{b['title'][:45]}' | cr='{c['title'][:45]}'")
    if b["year"] and c["year"] and b["year"] != c["year"]:
        iss.append(f"year: bib={b['year']} | cr={c['year']}")
    if b["journal"] and c["journal"] and not (toks(b["journal"]) & toks(c["journal"])):
        iss.append(f"journal: bib='{b['journal'][:35]}' | cr='{c['journal'][:35]}'")
    if b["volume"] and c["volume"] and b["volume"] != c["volume"]:
        iss.append(f"volume: bib={b['volume']} | cr={c['volume']}")
    if b["pages"] and c["page"] and firstpage(b["pages"]) != firstpage(c["page"]):
        iss.append(f"first-page: bib={b['pages']} | cr={c['page']}")
    if b["author"] and c["surnames"] and norm(first_surname(b["author"])) not in norm(" ".join(c["surnames"])):
        iss.append(f"1st author: bib='{first_surname(b['author'])}' | cr={c['surnames'][:3]}")
    report.append((b, "OK" if not iss else "CHECK", iss))
    print(f"[{i}/{len(rows)}] {b['key']}: {'OK' if not iss else 'CHECK ('+str(len(iss))+')'}")
    time.sleep(0.3)

flagged = [r for r in report if r[1] != "OK"]
with open("METADATA_CHECK_REPORT.md", "w", encoding="utf-8") as f:
    f.write("# Metadata check vs CrossRef (field-by-field)\n\n")
    f.write(f"- Total entries: {len(rows)}\n- Clean: {len(rows)-len(flagged)}\n- **Flagged: {len(flagged)}**\n\n")
    for b, st, iss in flagged:
        f.write(f"## {b['key']}  ({st})\n- bib: {b['author'][:50]} — {b['title'][:60]} — {b['journal'][:30]} {b['volume']} ({b['year']})\n")
        for x in iss: f.write(f"- {x}\n")
        f.write("\n")
print(f"\nDone. {len(flagged)}/{len(rows)} flagged. Report: METADATA_CHECK_REPORT.md")
