# Running and verifying the archive
## Verify the supplied materials without training
From the repository root, run:
```bash
python tools/check_archive.py
```
This uses only Python's standard library, parses Python/notebook files and checks the supplemental-source checksums. It does not import model libraries, scrape sites, fit models or establish reproduction of published metrics.

## Set up basic analysis tools
Use a separate virtual environment and install the basic analysis dependencies:
```bash
python -m venv .venv
# Activate .venv for your operating system, then:
python -m pip install -r requirements-analysis.txt
```
This unpinned list reflects the basic source imports; it is not an exact historical environment lock and does not guarantee compatibility of optional deep-learning variants.

## Project workflow and remaining dependencies
Start with the full recovered collection notebooks in notebooks/ and the script inventory in source/. Existing data/raw_scopus, data/research and data/university_archives cover original inputs and variants. Adapt input/output paths before running any script; source names may reference CSV conversions of the original XLSX files. Browser/page selectors are historical and not guaranteed against the current site. Do not run collection cells automatically when reviewing the archive. EmreAI is a design/report study, not an executable dependency.

## Evidence and scope
Original source archives and results are preserved. Packaging validation is separate from running the research. Missing original code, external data or hardware dependencies are documented rather than replaced with invented implementations.
