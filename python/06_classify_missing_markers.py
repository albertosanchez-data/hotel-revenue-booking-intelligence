
from pathlib import Path
import csv
from collections import Counter

# Locate the project folder.
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

FILES = ["H1.csv", "H2.csv"]
COLUMNS_TO_CHECK = ["Children", "Country", "Agent", "Company"]
CATEGORIES = ["EMPTY", "TEXT NULL", "OTHER VALUE"]


def classify_missing_markers(file_path):
    """Classify missing-value markers without modifying source files."""

    print("\n" + "=" * 60)
    print(f"FILE: {file_path.name}")
    print("=" * 60)

    if not file_path.is_file():
        print(f"ERROR: File not found: {file_path}")
        return

    try:
        with file_path.open(
            "r", encoding="utf-8-sig", newline=""
        ) as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                print("ERROR: The file is empty or has no header.")
                return

            missing_columns = [
                column
                for column in COLUMNS_TO_CHECK
                if column not in reader.fieldnames
            ]

            if missing_columns:
                print(
                    "ERROR: Required columns not found: "
                    + ", ".join(missing_columns)
                )
                return

            counts = {
                column: Counter()
                for column in COLUMNS_TO_CHECK
            }

            total_rows = 0
            malformed_rows = 0

            for row in reader:
                total_rows += 1

                # DictReader stores extra values under the None key.
                if (
                    None in row
                    or any(row.get(column) is None for column in COLUMNS_TO_CHECK)
                ):
                    malformed_rows += 1
                    continue

                for column in COLUMNS_TO_CHECK:
                    value = row[column].strip()

                    if value == "":
                        counts[column]["EMPTY"] += 1
                    elif value.upper() == "NULL":
                        counts[column]["TEXT NULL"] += 1
                    else:
                        counts[column]["OTHER VALUE"] += 1

    except (OSError, csv.Error, UnicodeError) as error:
        print(f"ERROR: Could not read the file: {error}")
        return

    valid_rows = total_rows - malformed_rows

    print(f"Total data rows: {total_rows}")
    print(f"Rows classified: {valid_rows}")
    print(f"Rows with structural problems: {malformed_rows}")

    for column in COLUMNS_TO_CHECK:
        print(f"\n{column}:")

        for category in CATEGORIES:
            count = counts[column][category]
            percentage = (
                count / valid_rows * 100 if valid_rows else 0
            )
            print(f"  {category}: {count} ({percentage:.2f}%)")


def main():
    """Classify missing-value markers in all source files."""

    print("HOTEL REVENUE & BOOKING INTELLIGENCE")
    print("Missing-marker classification")
    print("Original CSV files will not be modified.")

    for filename in FILES:
        classify_missing_markers(DATA_DIR / filename)


if __name__ == "__main__":
    main()
