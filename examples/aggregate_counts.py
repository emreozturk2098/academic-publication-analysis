"""Later educational aggregate example, not recovered CS552 scraping code."""
import csv
from collections import defaultdict


def totals_by_year(path):
    totals = defaultdict(int)
    seen = set()
    with open(path, encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            year = int(row["year"])
            count = int(row["article_count"])
            key = (row["institution"], year)
            if key in seen:
                raise ValueError("Duplicate institution/year aggregate")
            if count < 0:
                raise ValueError("Article counts must be non-negative")
            seen.add(key)
            totals[year] += count
    return dict(sorted(totals.items()))
