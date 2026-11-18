# Best Western Plus Edmonton Airport Hotel

<https://www.bwedmontonairporthotel.com/>

## Project overview

Website design, development, content, SEO, technical customization, and ongoing management for Best Western Plus Edmonton Airport Hotel in Leduc, Alberta, a 116-room property within Denham Hospitality Organization (DHO). The site shares a design system with its sister hotel, [Best Western Premier Denham Inn & Suites](../best-western-premier-denham/). The two sites cross-promote each other's dining and event spaces.

## My responsibilities

- Designed and built the website using Squarespace 7.1.
- Wrote and organized original website content.
- Developed SEO content and metadata.
- Customized layouts and presentation using CSS and HTML.
- Built structured data and AI-discoverability files.
- Manage and maintain the website.

## November 2026 audit and rebuild

I crawled all 20 pages and every link on them. Then I fixed what I found directly in Squarespace and re-crawled to confirm the fixes.

| Area | Found | Result |
|---|---|---|
| Links | 4 broken internal paths shared by up to 20 pages (copied from the Premier build), a dead `http://` link, a malformed Travel Alberta link, and an **Order Now** menu item that opened the sister hotel's restaurant | 0 broken internal links on re-crawl. 10 URL mappings, links corrected at the source, and Order Now pointed to Barney's ordering |
| Content left over from the Premier build | The Privacy Policy and Terms named the other hotel, with its address, phone and email. A hidden FAQ page was a full copy of the Premier FAQ | Both legal pages rewritten for this hotel, links included. The FAQ was rebuilt from scratch (below) |
| Live content gaps | Blank FAQ answers, "Suite occupancy TBC" showing to guests, an "Item description" placeholder, and a Park & Fly offer advertised with no package behind it | Answers filled from the hotel's Best Western listing. New **Park, Sleep & Fly** package card |
| Headings | 3 pages with two H1s, 1 page with none | One H1 per core page |
| Image alt text | 110 of 127 images | 127 of 127, including meaningful alt text for package icons |
| Metadata | 17 of 18 pages. The homepage title was only the hotel name | 18 of 18. The homepage now leads with "Leduc Hotel Near Edmonton Airport (YEG)" |
| Thin pages | Blog tag archives were indexable | `noindex, follow` on tag and category archives |
| Structured data | A basic `Hotel` entity only | Connected `@graph`: Denham Hospitality → Hotel → Barney's Pub & Grill, linked to the new `FAQPage` |
| AI discoverability | No `llms.txt` | [/llms.txt](https://www.bwedmontonairporthotel.com/llms.txt) published |
| Mobile | No persistent booking action | Bottom-pinned **Book Your Stay** bar on phones, shared with Premier |

## Master FAQ: one source, two outputs

The hotel's FAQ answers were scattered across six pages, the Best Western listing, Barney's website and the event-inquiry brochure, and some of those sources disagreed. I consolidated them into a single master FAQ: **68 questions in 14 topics**. Every on-page FAQ question is included.

The content lives in one Python data file. A small build script generates two outputs from it:

1. An accessible accordion. It uses native `<details>`/`<summary>` elements and topic jump links, and is styled with the site's own colour variables, so it follows any theme change.
2. Matching `FAQPage` JSON-LD, so the visible answers and the structured data can never drift apart.

[View the builder](../../technical-examples/faq-builder/)

Where the sources disagreed (event-room capacities, total event space, the restaurant's hours), I used the property-level figures and flagged each conflict for the general manager to confirm.

## Skills demonstrated

Squarespace 7.1 · Technical SEO audit · 301 redirects · Structured data (JSON-LD) · llms.txt · Content strategy · Copywriting · Information architecture · Accessibility · HTML/CSS · Python content tooling · Website management
