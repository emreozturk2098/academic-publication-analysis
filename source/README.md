# Full recovered coursework source

This archive contains **43 complete relevant Python scripts** from the recovered VSCode folder, not just the five excerpts. Original files are unchanged in the user's source workspace. Shared copies replace workstation-specific absolute path strings with relative placeholders; [the manifest](../docs/FULL_ARCHIVE_MANIFEST.json) records both original and shared hashes and the number of replacements.

| Folder | Purpose |
|---|---|
| [scraping_processing](scraping_processing) | Scopus/YÖK cleanup, joins, concatenation, department/institution/title summaries and historical demographic analyses |
| [yok_collection](yok_collection) | Historical Selenium collection for YÖK Academic Search, YÖK Atlas and university listings |
| [csv_conversion](csv_conversion) | CSV/Excel consolidation and row-count utilities |
| [processing](processing) | Author/affiliation parsing, institution type, publication/city/year summaries and plotting |

These are historical working scripts with several alternatives, not a single tested production pipeline. A later filename is not by itself proof that a script generated a particular figure. Existing imports vary: pandas, openpyxl, matplotlib, seaborn, selenium, unidecode, fuzzy matching and demographic-inference libraries as present in each file. No pinned historical environment was recovered; dependencies are not claimed to be locked.

Do not import entire scripts as libraries: many contain top-level file IO or browser startup. Inspect and configure file paths deliberately. Placeholder inputs under `data/inputs/` are not supplied automatically; available research workbooks are in [data/research](../data/research). Current browser selectors have not been tested. No scraping, full original-data processing or model training was run to package this archive.

Spectral reflectance/NIR/KNN scripts, model binaries and empty placeholders found in the same mixed folder belong outside this publication-analysis archive. [Selected excerpts](../examples/README.md) offer small in-memory entry points for reading the original logic.
