
from pathlib import Path
import csv

# Locate the project folder.
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

FILES = ["H1.csv", "H2.csv"]
MISSING_MARKERS = {"", "NULL", "NA", "N/A", "NONE", "NAN"}


def profile_missing_values(file_path):
    """Count missing and NULL-like values without changing source data."""

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
            reader = csv.reader(file)
            header = next(reader, None)

            if not header:
                print("ERROR: The file is empty or has no header.")
                return

            if any(not column.strip() for column in header):
                print("WARNING: One or more column names are empty.")

            missing_counts = {column: 0 for column in header}
            total_rows = 0
            valid_rows = 0
            malformed_rows = 0

            for row in reader:
                total_rows += 1

                if len(row) != len(header):
                    malformed_rows += 1
                    continue

                valid_rows += 1

                for column, value in zip(header, row):
                    if value.strip().upper() in MISSING_MARKERS:
                        missing_counts[column] += 1

    except (OSError, csv.Error, UnicodeError) as error:
        print(f"ERROR: Could not read the file: {error}")
        return

    print(f"Total data rows: {total_rows}")
    print(f"Rows analyzed: {valid_rows}")
    print(f"Rows with incorrect column count: {malformed_rows}")

    print("\nColumns with missing or NULL-like values:")

    found_missing = False

    for column, count in missing_counts.items():
        if count > 0:
            percentage = (
                count / valid_rows * 100 if valid_rows else 0
            )
            print(f"{column}: {count} ({percentage:.2f}%)")
            found_missing = True

    if not found_missing:
        print("None detected")


def main():
    """Profile missing values in each source CSV file."""

    print("HOTEL REVENUE & BOOKING INTELLIGENCE")
    print("Missing-value profiling")
    print("Original CSV files will not be modified.")

    for filename in FILES:
        profile_missing_values(DATA_DIR / filename)


if __name__ == "__main__":
    main()
