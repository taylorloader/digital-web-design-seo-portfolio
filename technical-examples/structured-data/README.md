# Structured data (JSON-LD / Schema.org)

Hand-written JSON-LD added through Squarespace page-level code injection, layered on top of the platform's default `WebSite` / `Organization` / `LocalBusiness` output.

## Best Western Premier Denham Inn & Suites

The entities are linked by stable `@id` values, so search engines and AI tools read them as one connected picture rather than separate fragments:

```
Denham Hospitality (Organization)  #denham-hospitality
        │ parentOrganization
        ▼
Best Western Premier Denham Inn & Suites (Hotel)  #hotel  ◄── publisher ── WebSite #website
        │ containsPlace                         ▲
        ├── O'Brian's Restaurant & Grill (Restaurant)   │ containedInPlace
        └── Jonathan's Lounge (BarOrPub)          ──────┘
        ▲ provider
        ├── Weddings (Service)
        └── Meetings & Corporate Events (Service)
FAQ (FAQPage, 127 questions) ── about ──► Hotel
```

| Page | Schema | Purpose |
|---|---|---|
| Homepage | `@graph` of `Organization`, `WebSite`, `Hotel` | Operator, brand, address, contact, logo, photo, social profiles, amenities, on-site venues |
| O'Brian's Restaurant & Grill | `Restaurant` | On-site dining, linked back to the hotel |
| Jonathan's Lounge | `BarOrPub` | On-site lounge, linked back to the hotel |
| Weddings | `Service` | Wedding venue and reception services |
| Meetings & Corporate Events | `Service` | Meeting rooms and corporate events |
| FAQ | `FAQPage` | 127 questions and answers taken from the visible page content |

Facts are kept consistent across the schema, the visible pages and [`/llms.txt`](../ai-discoverability/). The homepage validates with **0 errors and 0 warnings** in the [Schema.org validator](https://validator.schema.org/).

## Examples

- [premier-hotel.jsonld](premier-hotel.jsonld): the homepage `@graph`.

All examples contain only public business information already published on the live site.
