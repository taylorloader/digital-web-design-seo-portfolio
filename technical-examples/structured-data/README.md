# Structured data (JSON-LD / Schema.org)

Hand-written JSON-LD added through Squarespace code injection to describe each property and its key services as linked entities, on top of the platform's default `WebSite` / `Organization` / `LocalBusiness` output.

## Best Western Premier Denham Inn & Suites

| Page | Schema type | Purpose |
|---|---|---|
| Homepage | `Hotel` with `PostalAddress` and `LocationFeatureSpecification` amenities | Primary entity: address, phone, check-in / check-out and amenities |
| O'Brian's Restaurant & Grill | `Restaurant` | On-site dining venue |
| Weddings | `Service` | Wedding venue and catering offering |

Each entity uses a stable `@id` (for example `https://www.bestwesterndenham.com/#hotel`) so the entities can reference one another and stay consistent across pages.

## Examples

- [premier-hotel.jsonld](premier-hotel.jsonld) — the homepage `Hotel` entity.

All examples contain only public business information already published on the live site.
