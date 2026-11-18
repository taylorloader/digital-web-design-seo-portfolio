# AI discoverability: llms.txt

`llms.txt` is a plain-Markdown file served at a site's root that gives large language models and AI answer engines a clean, curated summary of a website: who the business is, the facts that matter, and the pages worth reading.

## What I implemented

- Published `/llms.txt` on [bestwesterndenham.com](https://www.bestwesterndenham.com/llms.txt) (Squarespace 7.1).
- Kept the facts in the file consistent with the site's JSON-LD `Hotel` entity (address, telephone, check-in / check-out, amenities), so search engines and AI tools receive the same answer from both sources.
- Confirmed the site's `robots.txt` permits the major AI crawlers (GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, PerplexityBot and others), so the file can actually be read.
- Structured the file to the [llms.txt proposal](https://llmstxt.org/): H1 name, blockquote summary, key facts, then H2 sections of annotated Markdown links, with lower-priority pages under `## Optional`.

## Example

- [premier-llms.txt](premier-llms.txt) — the Best Western Premier Denham Inn & Suites file.

## Why it matters for a hotel

Travellers increasingly ask AI assistants questions like "hotel with a free shuttle near Edmonton airport" or "wedding venue in Leduc." A curated `llms.txt`, matching structured data and crawlable pages give those tools accurate, first-party information instead of leaving them to piece it together from third-party listings.
