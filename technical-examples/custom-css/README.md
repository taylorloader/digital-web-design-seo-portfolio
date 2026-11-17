# Custom CSS — Squarespace 7.1

This section documents selected front-end styling work for the Best Western Premier Denham Inn & Suites website.

## Button interaction system

A central feature of the stylesheet is a coordinated button system with three visual treatments:

| Button type | Resting appearance | Desktop hover appearance |
|---|---|---|
| Primary | Deep red with layered gradient detail | Champagne / gold with dark text |
| Secondary | Light champagne / gold with dark text | Deep red with light text |
| Tertiary | Translucent, blurred-glass treatment | Champagne / gold with dark text |

The system also includes:

- Shared spacing, sizing, transition, and shadow rules.
- A subtle vertical lift and stronger shadow on desktop hover.
- A visible keyboard focus outline.
- Touch-specific active and resting states for devices without hover.
- Separate link styling so standard text-link hover behavior does not interfere with button appearance.

## Additional refinements

The broader stylesheet includes targeted rules for selected Squarespace components:

- Link and footer-link behavior.
- Rich-text / HTML-block checklists with inline gold checkmarks.
- Rounded corners on selected image, gallery, summary, and carousel media.
- Footer newsletter spacing and field dimensions.
- Mobile menu colors.
- Hero introduction list spacing.

## Implementation notes

The stylesheet uses CSS custom properties for the core red, neutral, and champagne/gold palette, along with reusable shadow and transition values. This supports consistent styling and makes global refinements easier.

The code is written for Squarespace 7.1's existing elements and class names. It is CSS customization, not a JavaScript application or a replacement for Squarespace's platform functionality.

## Portfolio publishing

Before adding full source snippets, review them for any private URLs, internal identifiers, or business-specific details that should not be public. Publish only code that you authored or are authorized to share.
