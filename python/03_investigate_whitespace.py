
from pathlib import Path
import csv

# Locate the project folder.
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

FILES = ["H1.csv", "H2.csv"]


def inspect_spaces(file_path):
    """Detect leading and trailing spaces without changing source data."""

    print("\n" + "=" * 60)
    print(f"FILE: {file_path.name}")
    print("=" * 60)

    # Check whether the source file exists.
    if not file_path.is_file():
        print(f"ERROR: File not found: {file_path}")
        return

    try:
        with file_path.open(
            "r", encoding="utf-8-sig", newline=""
        ) as file:
            reader = csv.reader(file)

            # Read and validate the header.
            header = next(reader, None)

            if not header:
                print("ERROR: The file is empty or has no header.")
                return

            if any(not column.strip() for column in header):
                print("WARNING: One or more column names are empty.")

            leading_spaces = {column: 0 for column in header}
            trailing_spaces = {column: 0 for column in header}

            total_rows = 0
            valid_rows = 0
            malformed_rows = 0

            # Inspect each row without modifying its values.
            for row in reader:
                total_rows += 1

                if len(row) != len(header):
                    malformed_rows += 1
                    continue

                valid_rows += 1

                for column, value in zip(header, row):
                    if value != value.lstrip():
                        leading_spaces[column] += 1

                    if value != value.rstrip():
                        trailing_spaces[column] += 1

    except (OSError, csv.Error, UnicodeError) as error:
        print(f"ERROR: Could not read the file: {error}")
        return

    print(f"Total data rows: {total_rows}")
    print(f"Rows inspected: {valid_rows}")
    print(f"Rows with incorrect column count: {malformed_rows}")

    print("\nColumns with leading spaces:")
    found_leading = False

    for column, count in leading_spaces.items():
        if count > 0:
            print(f"  {column}: {count} values")
            found_leading = True

    if not found_leading:
        print("  None detected")

    print("\nColumns with trailing spaces:")
    found_trailing = False

    for column, count in trailing_spaces.items():
        if count > 0:
            print(f"  {column}: {count} values")
            found_trailing = True

    if not found_trailing:
        print("  None detected")


def main():
    """Inspect whitespace in all configured source files."""

    print("HOTEL REVENUE & BOOKING INTELLIGENCE")
    print("Source data whitespace investigation")
    print("Original CSV files will not be modified.")

    for filename in FILES:
        inspect_spaces(DATA_DIR / filename)


if __name__ == "__main__":
    main()
