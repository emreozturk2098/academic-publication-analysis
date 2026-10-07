# Graduate academic-publication data study
CS552.A Data Science with Python, Özyeğin University, during Emre Öztürk's master's studies. Emre Öztürk and Ali Baki Türköz worked jointly and equally at every stage, confirmed by Emre.

## Question and method
The study investigated how recorded academic publication counts vary across years, cities, university types and departments. Course sources describe Scopus records matched with university/faculty/department information from YÖK Atlas. Cleanup included name-order correction, Turkish/English character normalization, spelling variants and matching intended to use names and institution context. The recovered selected prototype joins on names alone; affiliation extraction exists separately, but a combined institution-validated match is not demonstrated by that excerpt. Text normalization is a processing step, not proof of correct entity resolution.

The source covers author-level records and additional demographic analysis. This private school archive now includes available original matched-author/reference workbooks, full relevant scripts, reports and distinct aggregate figures. Inferred demographic labels in the historical data are not independently verified. No current scraping or personal-data enrichment is performed.

## What is available
The presentation and report draft describe the workflow; original aggregate PNG outputs survive. The earlier Word source contained placeholders. Original Python scripts were subsequently recovered from the VSCode archive. They include Selenium collection from YÖK Atlas and YÖK Academic Search, textual cleanup, author/affiliation processing, prototype joins and aggregate analysis. This package now shares selected original functions and matching statements, and also the complete relevant scripts plus available original matched-author/reference workbooks. The later aggregate illustration and synthetic data remain separately labeled.

## Scope and interpretation
The materials describe different ranges (1900s in the broad objective, 1970 onward in the annual figure, post-1990 in the department figure). These are distinct views, not one silently reconciled dataset. The report mentions responsibility for seven cities in some analyses; completeness of national coverage is not independently established. The department plot filters counts of at least 3,000; low-count departments are omitted from that view.

Article totals may reflect author-affiliation counting and duplicate/coauthor joins; the recovered scripts help inspect processing decisions, but a complete linkage between the archived figures, exact run inputs and deduplication steps has not been established. Do not call every bar a count of unique national papers. Publication counts are descriptive; they do not establish publication quality, causal policy effects or interdisciplinary collaboration. The 2024 collection date/completeness is not verified.

Third-party Türkiye Bilim/Diaspora reports in the workspace are background references, not the team's original outputs. EmreAI is a separate design/report exercise and is not mixed into this data-analysis repo. No published paper or deployed system is claimed.

The repo stays private. Available school-project data and full relevant scripts are included; some raw Scopus inputs remain unavailable. Contact: emre.ozturk.2098@gmail.com.
