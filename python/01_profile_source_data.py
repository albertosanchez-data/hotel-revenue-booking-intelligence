
import csv
from pathlib import Path
from collections import Counter

# Locate the project and source data folder.
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

FILES = ["H1.csv", "H2.csv"]
NULL_VALUES = {"", "NULL", "NA", "N/A", "NONE", "NAN"}


def profile_file(file_path):
    print("\n" + "=" * 65)
    print(f"FILE: {file_path.name}")
    print("=" * 65)

    if not file_path.exists():
        print(f"ERROR: File not found: {file_path}")
        return

    row_count = 0
    malformed_rows = 0
    duplicate_rows = 0
    missing_counts = Counter()
    seen_rows = set()
    headers = []

    with file_path.open(
        "r", encoding="utf-8-sig", newline=""
    ) as file:
        reader = csv.reader(file)

        try:
            headers = next(reader)
        except StopIteration:
            print("ERROR: The file is empty.")
            return

        headers = [header.strip() for header in headers]
        expected_columns = len(headers)

        for row in reader:
            row_count += 1

            if len(row) != expected_columns:
                malformed_rows += 1
                continue

            # Count exact duplicate records without removing them.
            row_key = tuple(row)
            if row_key in seen_rows:
                duplicate_rows += 1
            else:
                seen_rows.add(row_key)

            # Count empty or NULL-like values by column.
            for header, value in zip(headers, row):
                if value.strip().upper() in NULL_VALUES:
                    missing_counts[header] += 1

    print(f"Column count: {expected_columns}")
    print(f"Data rows: {row_count}")
    print(f"Rows with unexpected column counts: {malformed_rows}")
    print(f"Exact repeated rows after the first occurrence: {duplicate_rows}")

    print("\nMissing or NULL-like values by column:")
    found_missing = False

    for header in headers:
        count = missing_counts[header]
        if count > 0:
            print(f"  {header}: {count}")
            found_missing = True

    if not found_missing:
        print("  None detected")

    print("\nColumn names:")
    print(", ".join(headers))


def main():
    print("HOTEL REVENUE & BOOKING INTELLIGENCE")
    print("Initial source data profiling")
    print("Original CSV files will not be modified.")

    for filename in FILES:
        profile_file(DATA_DIR / filename)


if __name__ == "__main__":
    main()
