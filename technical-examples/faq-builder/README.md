# FAQ builder

Single-source build for the [Best Western Plus Edmonton Airport Hotel FAQ](https://www.bwedmontonairporthotel.com/faq).

- [`faq_data.py`](faq_data.py): 68 questions in 14 topics, consolidated from every on-page FAQ on the site, the hotel's Best Western listing, the restaurant's website and the event brochure.
- [`build_faq.py`](build_faq.py): generates both outputs below from that one file, so the visible answers and the structured data always match.
  - [`airport-faq-codeblock.html`](airport-faq-codeblock.html): an accessible accordion built with native `<details>`/`<summary>` elements, plus topic jump links, styled with the site's theme variables and pasted into one Squarespace Code Block.
  - [`airport-faq.jsonld`](airport-faq.jsonld): the `FAQPage` schema, linked by `@id` to the hotel entity in [structured-data](../structured-data/).

Run it with: `python3 build_faq.py`
