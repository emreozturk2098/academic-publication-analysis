# Selected original code and later illustration

Original Python scripts were recovered from `VSCode_Kodları` on 7 October 2026. The earlier `CS552_Project1_Codes.docx` was a placeholder document; the previous claim that no original code survives is superseded.

| File | Provenance and purpose |
|---|---|
| [original_text_normalization.py](original_text_normalization.py) | Unchanged original functions from `scopus_all_upper.py`: Turkish-character conversion and numeric-parenthesis cleanup. |
| [original_author_affiliation_cleaning.py](original_author_affiliation_cleaning.py) | Unchanged original functions from `deneme13.py`: author-name formatting, university affiliation filtering and city substring extraction. |
| [original_name_formatting.py](original_name_formatting.py) | Unchanged original functions from `Matching_csvler.py`: parenthesis removal and the historical comma-name ordering rule. |
| [original_matching_excerpt.py](original_matching_excerpt.py) | Original selected pandas statements from `Matching_csvler.py`, enclosed in a new in-memory function wrapper; local CSV reads/writes removed. Requires pandas and the sibling name-formatting excerpt. |
| [original_pagination_xpath.py](original_pagination_xpath.py) | Unchanged historical `get_page_xpath` function used by a YÖK Academic Search Selenium script. It does not start a browser, collect data or access a saved browser profile. |
| [aggregate_counts.py](aggregate_counts.py) | Later portfolio illustration using only fabricated institution/year data. This is not original recovered analysis code. |

SHA-256 source hashes and exact selected line ranges are recorded in [the source manifest](../docs/SOURCE_MANIFEST.json). The original research files are unchanged. Selected pure functions and the name-only join were checked using synthetic inputs; no real academic records were processed and no scraper was run.

Historical limitations are preserved rather than silently fixed: the character converter includes an uppercase `I` to lowercase `i` mapping; comma-name parsing reverses two given names; author cleanup omits non-comma formatted entries; university filtering looks for the literal word `University`; city matching is a case-sensitive substring search; name-only joins can collide or expand duplicate matches. Final matching selects/deduplicates names, not unique publication IDs. These excerpts are a case study in the original workflow, not a production identity-resolution service.

The pagination XPath assumes historical page structure and contains brittle page-number rules. Its behavior against the current website was not tested. Full relevant scripts and available research records are now supplied separately in the private school archive. Browser-profile paths are replaced with relative placeholders, and unrelated spectral model binaries are not included. [Recovered-code scope and caveats](../docs/RECOVERED_CODE.md).
