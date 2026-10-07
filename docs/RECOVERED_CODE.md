# Recovered code: evidence and scope

## What changed

The newly supplied VSCode archive contains actual Python scripts. The previous portfolio was based on reports, plots and a placeholder Word document. The repository now distinguishes **selected recovered original code** from the **later synthetic aggregate example**.

The archive includes Selenium scripts for YÖK Atlas university/program extraction and YÖK Academic Search author/title/department collection; Scopus CSV consolidation; Turkish-character normalization and author-name formatting; prototype joins; university/affiliation/city extraction; institution/department/city aggregation and plotting. Source inspection does not establish that every script was used in the final submitted analysis.

The folder also contains wavelength/reflectance and KNN spectral scripts and model binaries. They are not automatically classified as CS552 publication-analysis work and were not added to this repository. The historical `SCOPUS_KODLAR.docx` contains prose rather than the actual Python implementation. The recovered `.py` files provide the code evidence.

## Included selection

Five small excerpts cover normalization, author/affiliation cleanup, name formatting, name-only matching and historic pagination logic. Functions are unchanged where documented; the matching statements have a new in-memory wrapper so no local path or data-file execution is required. Imports and headers are added for standalone use. Complete file input/output loops, raw records and the full collection scripts are withheld.

## Findings that limit interpretation

- The selected name-matching script joins on normalized names alone, then keeps/deduplicates names. It does not enforce an institution key or retain unique publication IDs. Namesakes and many-to-many matches remain possible.
- Affiliation/city parsing exists in a different script; its existence does not prove the final join combined name and institution consistently.
- One city/year analysis explodes semicolon-separated city values and counts rows; another constructs a city × inferred-gender Cartesian product. These are different counting units, not automatically unique article totals.
- The selected pagination function comes from YÖK Academic Search, not YÖK Atlas. Source comments mention 22 pages while the loop runs up to 130; hardcoded row selection, absolute XPath and 0.1-second waits are historical implementation limits.
- No one-to-one match has yet been established between these individual script versions and the four retained archived figures. The source figure captions and coverage limitations remain valid.

No browser was launched by the recovered scripts, no scraping ran, no saved browser profile was accessed, no original data analysis was rerun and no new research score was produced for this portfolio update. Original files were not modified. Full material requests: **emre.ozturk.2098@gmail.com**. The repository remains **private**.


## Expanded school archive (supersedes the initial excerpt-only distribution scope)
Emre authorized full relevant school-project materials. Complete relevant scripts, available original workbooks, original course reports and all distinct publication-analysis PNGs are now included; see FULL_ARCHIVE_MANIFEST.json. The original selected-only statements above describe the earlier package. Raw historical Scopus inputs remain unlocated, so end-to-end reproduction is still not claimed.


## Expanded school archive (supersedes the initial excerpt-only distribution scope)
Emre authorized full relevant school-project materials. Complete relevant scripts, available original workbooks, original course reports and all distinct publication-analysis PNGs are now included; see FULL_ARCHIVE_MANIFEST.json. The original selected-only statements above describe the earlier package. Raw historical Scopus inputs remain unlocated, so end-to-end reproduction is still not claimed.
