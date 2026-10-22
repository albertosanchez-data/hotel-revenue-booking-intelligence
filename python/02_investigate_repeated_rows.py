
from pathlib import Path
import csv
from collections import Counter

# Locate the project folder.
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

FILES = ["H1.csv", "H2.csv"]


def investigate_file(file_path):
    """Investigate exact repeated rows without modifying the source file."""

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

            row_counts = Counter()
            total_rows = 0
            malformed_rows = 0

            # Count rows while validating their column count.
            for row in reader:
                total_rows += 1

                if len(row) != len(header):
                    malformed_rows += 1
                    continue

                row_counts[tuple(row)] += 1

    except (OSError, csv.Error, UnicodeError) as error:
        print(f"ERROR: Could not read the file: {error}")
        return

    # Identify exact repeated row patterns.
    repeated_rows = {
        row: count
        for row, count in row_counts.items()
        if count > 1
    }

    repeated_extra_rows = sum(
        count - 1 for count in repeated_rows.values()
    )

    print(f"Total data rows: {total_rows}")
    print(f"Rows with incorrect column count: {malformed_rows}")
    print(f"Rows analyzed: {sum(row_counts.values())}")
    print(f"Distinct row patterns: {len(row_counts)}")
    print(
        "Row patterns appearing more than once: "
        f"{len(repeated_rows)}"
    )
    print(
        "Rows beyond the first occurrence: "
        f"{repeated_extra_rows}"
    )

    print("\nTop 3 most frequent exact row patterns:")

    if not row_counts:
        print("No valid data rows available for analysis.")
        return

    for number, (row, count) in enumerate(
        row_counts.most_common(3), start=1
    ):
        print(f"\nExample {number}: appears {count} times")

        for column, value in zip(header, row):
            print(f"  {column}: {value}")


def main():
    """Run the investigation for each source file."""

    print("HOTEL REVENUE & BOOKING INTELLIGENCE")
    print("Exact repeated-row investigation")
    print("Source CSV files will not be modified.")

    for filename in FILES:
        investigate_file(DATA_DIR / filename)


if __name__ == "__main__":
    main()
