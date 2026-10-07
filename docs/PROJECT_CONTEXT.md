# Graduate academic-publication data study
CS552.A Data Science with Python, Özyeğin University, during Emre Öztürk's master's studies. Emre Öztürk and Ali Baki Türköz worked jointly and equally at every stage, confirmed by Emre.

## Question and method
The study investigated how recorded academic publication counts vary across years, cities, university types and departments. Course sources describe Scopus records matched with university/faculty/department information from YÖK Atlas. Cleanup included name-order correction, Turkish/English character normalization, spelling variants and matching using both name and institution to reduce homonym confusion. Text normalization is a processing step, not proof of correct entity resolution.

The source covers author-level records and additional demographic analysis. This selected portfolio shares only institution/city/year/department aggregate figures. Personal names, inferred demographic labels and raw matching workbooks are excluded. No current scraping or personal-data enrichment is performed.

## What is available
The presentation and report draft describe the workflow; original aggregate PNG outputs survive. The source Word code file contains placeholders, so the historical scraper and author matching cannot be reproduced from this package. A small later code illustration and synthetic aggregate input explain the form of processing without pretending to recreate the historical implementation.

## Scope and interpretation
The materials describe different ranges (1900s in the broad objective, 1970 onward in the annual figure, post-1990 in the department figure). These are distinct views, not one silently reconciled dataset. The report mentions responsibility for seven cities in some analyses; completeness of national coverage is not independently established. The department plot filters counts of at least 3,000; low-count departments are omitted from that view.

Article totals may reflect author-affiliation counting and duplicate/coauthor joins; the missing implementation prevents independently verifying the counting unit and deduplication. Do not call every bar a count of unique national papers. Publication counts are descriptive; they do not establish publication quality, causal policy effects or interdisciplinary collaboration. The 2024 collection date/completeness is not verified.

Third-party Türkiye Bilim/Diaspora reports in the workspace are background references, not the team's original outputs. EmreAI is a separate design/report exercise and is not mixed into this data-analysis repo. No published paper or deployed system is claimed.

The repo stays private. Full source data and original code are not distributed. Contact: emre.ozturk.2098@gmail.com.
