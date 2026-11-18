# Technical SEO

Fixes from a full crawl of [bestwesterndenham.com](https://www.bestwesterndenham.com/): every page in the sitemap fetched and every link on it checked.

## Audit and fixes (November 2026)

| Area | Found | Fixed |
|---|---|---|
| Links | 8 broken or incorrect links across 79 pages (5 internal 404s, a contact email linked to squarespace.com, a malformed link, a dead external domain), plus one link to the Squarespace build domain | 0 broken links on re-crawl. 5 permanent redirects added and links corrected at the source |
| Headings | 5 pages with more than one H1, and O'Brian's with no visible H1 | One visible H1 per core page |
| Image alt text | 21 of 332 images missing | 332 of 332 |
| Page titles | Brand repeated on every inner page (`%p — %s`), some titles over 100 characters, a weak FAQ title | Title format set to the page's own SEO title. Homepage, FAQ and Location titles rewritten around search intent |
| Thin pages | ~42 blog tag archives indexable | `noindex, follow` on tag and category archives |
| Structured data | Disconnected entities, an address mismatch, a broken `@id` and URL on the Weddings schema | Connected `@graph`, consistent address, new `FAQPage` and Meetings `Service` |

## Lighthouse baseline (homepage, 18 Nov 2026)

| | Mobile | Desktop |
|---|---|---|
| SEO | 100 | |
| Accessibility | 95 | |
| Best Practices | 96 | |
| Performance | 39 | 63 |

Performance is limited mainly by the full-screen hero video, which stays for brand reasons, and by the platform's own scripts.

## Code

- [url-mappings.txt](url-mappings.txt): the 301 redirect rules.
- [noindex-tag-archives.html](noindex-tag-archives.html): the blog header script that keeps tag archives out of search.
