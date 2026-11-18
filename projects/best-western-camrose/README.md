# Best Western Plus Rose Country Hotel, Camrose

<https://www.bestwesterncamrose.com/>

## Project overview

Website design, development, content, SEO, technical customization, and ongoing management for Best Western Plus Rose Country Hotel in Camrose, Alberta. It is a 112-room property within Denham Hospitality Organization (DHO), with an on-site restaurant (Rosie's Kitchen), a lounge (Joker's Den) and the attached Camrose Resort Casino. The site was built from the Premier template, so the audit focused on anything the copy carried over.

## My responsibilities

- Designed and built the website using Squarespace 7.1.
- Wrote and organized original website content.
- Developed SEO content and metadata.
- Customized layouts and presentation using CSS and HTML.
- Built structured data and AI-discoverability files.
- Manage and maintain the website.

## November 2026 audit and rebuild

I crawled all 33 pages and every internal link on them. Then I fixed what I found directly in Squarespace and re-crawled to confirm the fixes.

| Area | Found | Result |
|---|---|---|
| Links | The weddings jump menu sent guests to the Leduc wedding page, plus a link to Premier's Squarespace build address. 3 **Explore Venue** buttons opened Premier ballrooms. The lounge's **Let's Eat!** button went to Premier's restaurant (404 here) | 0 broken internal links on re-crawl. Jump links and buttons now land on sections of the Camrose page, and Let's Eat! opens Rosie's Kitchen |
| Redirects | None | 12 URL mappings: safety nets for the paths copied from the Premier build, plus short shareable URLs (`/rooms`, `/weddings`, `/careers` …). All 12 verified as 301 |
| Content left over from the Premier build | The Privacy Policy and Terms named Best Western Premier Denham Inn & Suites, and the privacy address read "3201 28th Avenue". The FAQ linked to "the Denham Inn" | Both legal pages and the FAQ now name this hotel, with the correct address (3201 48th Avenue) |
| Titles | The site name was appended to every page title, so 30 of 33 titles ran past 70 characters | Title format set to each page's own SEO title. 1 title left over 75 characters |
| Headings | 2 core pages with no H1, 2 with two | One H1 per core page |
| Image alt text and metadata | Already complete | 394 of 394 images with alt text, 25 of 25 pages with metadata, Squarespace search visibility 98% |
| Thin pages | 5 blog tag archives were indexable, including case duplicates (Food / food) | `noindex, follow` on tag and category archives, verified live |
| Structured data | A basic `LocalBusiness` entity. No FAQ markup | Connected `@graph`: Denham Hospitality → Hotel → Rosie's Kitchen, Joker's Den (with hours) and Camrose Resort Casino. `FAQPage` markup for all 41 FAQ answers |
| AI discoverability | No `llms.txt` | [/llms.txt](https://www.bestwesterncamrose.com/llms.txt) published |
| Mobile | No persistent booking action | Bottom-pinned **Book Your Stay** bar on phones, shared with Premier and the Airport hotel |

## One organization, three hotels

All three hotel sites now point their structured data to the same `Organization` node on bestwesterndenham.com. Search engines and AI assistants can read the three properties as one hotel group, and each hotel's restaurant, lounge or casino as part of that hotel rather than as a separate business.

- [Camrose schema](../../technical-examples/structured-data/camrose-hotel.jsonld)
- [Camrose llms.txt](../../technical-examples/ai-discoverability/camrose-llms.txt)
- [Redirect rules](../../technical-examples/technical-seo/url-mappings.txt)

## Flagged for the property team

- Restaurant hours and breakfast pricing on the Best Western listing differ from the site, and need confirming before either is changed.
- Menu and brochure PDFs are linked from a company OneDrive. They are being checked for public access.

## Skills demonstrated

Squarespace 7.1 · Technical SEO audit · 301 redirects · Structured data (JSON-LD) · llms.txt · Information architecture · Content QA · HTML/CSS · Website management
