"""Build the Airport Hotel FAQ code block: accessible <details> accordion + FAQPage JSON-LD from one source."""
import json, re, html
from faq_data import FAQ

SITE = "https://www.bwedmontonairporthotel.com"

def plain(s):
    s = re.sub(r"</li>", "; ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(re.sub(r"\s+", " ", s)).strip()
    return re.sub(r"\s+([.,;:])", r"\1", s).replace(":;", ":").replace("; .", ".")

css = """<style>
@media (min-width:768px){.fe-block:has(.bwfaq){grid-area:7/2/8/26!important}}
.bwfaq{--ac:hsl(var(--accent-hsl,345,70%,32%));--ink:hsl(var(--black-hsl,0,0%,12%));max-width:920px;margin:0 auto;color:var(--ink)}
.bwfaq-nav{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 40px;padding:0;list-style:none}
.bwfaq-nav a{display:inline-block;padding:8px 14px;border:1px solid var(--ac);border-radius:999px;color:var(--ac);text-decoration:none;font-size:14px;line-height:1.2;transition:background .2s,color .2s}
.bwfaq-nav a:hover,.bwfaq-nav a:focus-visible{background:var(--ac);color:#fff}
.bwfaq h2{margin:48px 0 12px;scroll-margin-top:120px}
.bwfaq details{border-bottom:1px solid hsla(var(--black-hsl,0,0%,12%),.15)}
.bwfaq summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:16px;padding:18px 0;font-weight:500;font-size:1.05em}
.bwfaq summary::-webkit-details-marker{display:none}
.bwfaq summary::after{content:"+";color:var(--ac);font-size:1.4em;line-height:1;transition:transform .2s}
.bwfaq details[open] summary::after{transform:rotate(45deg)}
.bwfaq summary:focus-visible{outline:2px solid var(--ac);outline-offset:4px}
.bwfaq .a{padding:0 0 20px;line-height:1.65}
.bwfaq .a a{color:var(--ac)}
.bwfaq .a ul{margin:10px 0 10px 20px;padding:0}
.bwfaq .cta{margin:56px 0 0;padding:28px;background:#fff;border-radius:6px;text-align:center}
@media (max-width:767px){.bwfaq h2{margin-top:36px}.bwfaq-nav{gap:6px}.bwfaq-nav a{font-size:13px;padding:7px 12px}}
</style>"""

nav = "".join(f'<li><a href="#{sid}">{title}</a></li>' for sid, title, _ in FAQ)
body = []
for sid, title, items in FAQ:
    body.append(f'<h2 id="{sid}">{title}</h2>')
    for q, a in items:
        body.append(f"<details><summary>{q}</summary><div class=\"a\">{a}</div></details>")

schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "@id": f"{SITE}/faq#faqpage",
    "url": f"{SITE}/faq",
    "name": "Hotel FAQ | Best Western Plus Edmonton Airport Hotel, Leduc",
    "inLanguage": "en-CA",
    "about": {"@id": f"{SITE}/#hotel"},
    "isPartOf": {"@id": f"{SITE}/#website"},
    "mainEntity": [
        {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
        for _, _, items in FAQ for q, a in items
    ],
}

cta = ('<div class="cta"><p><strong>Still have a question?</strong> Our front desk is open 24 hours.</p>'
       '<p><a href="tel:+17809866550">(780) 986-6550</a> · '
       '<a href="mailto:plusguestservices@denhamhotels.com">plusguestservices@denhamhotels.com</a></p></div>')

out = (css + '<div class="bwfaq"><nav aria-label="FAQ topics"><ul class="bwfaq-nav">' + nav + "</ul></nav>"
       + "".join(body) + cta + "</div>"
       + '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False, separators=(",", ":")) + "</script>")
open("airport-faq-codeblock.html", "w").write(out)
open("airport-faq.jsonld", "w").write(json.dumps(schema, ensure_ascii=False, indent=2))
print(len(out), "chars;", len(schema["mainEntity"]), "questions")
