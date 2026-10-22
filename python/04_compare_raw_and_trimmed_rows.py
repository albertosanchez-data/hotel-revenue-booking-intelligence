
from pathlib import Path
import csv
from collections import Counter

# Locate the project folder.
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

FILES = ["H1.csv", "H2.csv"]

COLUMNS_TO_SAMPLE = [
    "IsRepeatedGuest",
    "Agent",
    "Company",
    "Meal",
    "ReservedRoomType",
    "AssignedRoomType",
    "DepositType",
]


def compare_rows(file_path):
    """Compare exact row patterns before and after trimming whitespace."""

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

            rows = []
            malformed_rows = 0

            for row in reader:
                if len(row) != len(header):
                    malformed_rows += 1
                    continue

                rows.append(tuple(row))

    except (OSError, csv.Error, UnicodeError) as error:
        print(f"ERROR: Could not read the file: {error}")
        return

    # Trim values in memory only; source CSV files remain unchanged.
    trimmed_rows = [
        tuple(value.strip() for value in row)
        for row in rows
    ]

    raw_patterns = Counter(rows)
    trimmed_patterns = Counter(trimmed_rows)

    # Count raw patterns that become the same after trimming.
    raw_to_trimmed = {}
    for raw_row, count in raw_patterns.items():
        trimmed_row = tuple(value.strip() for value in raw_row)
        raw_to_trimmed.setdefault(trimmed_row, []).append(
            (raw_row, count)
        )

    merged_groups = sum(
        len(raw_versions) > 1
        for raw_versions in raw_to_trimmed.values()
    )

    print(f"Total data rows: {len(rows) + malformed_rows}")
    print(f"Rows analyzed: {len(rows)}")
    print(f"Rows with incorrect column count: {malformed_rows}")
    print(f"Distinct raw patterns: {len(raw_patterns)}")
    print(f"Distinct patterns after trimming: {len(trimmed_patterns)}")
    print(f"Groups merged by trimming: {merged_groups}")

    print("\nPatterns appearing more than once:")
    print(
        "Before trimming: "
        f"{sum(count > 1 for count in raw_patterns.values())}"
    )
    print(
        "After trimming:  "
        f"{sum(count > 1 for count in trimmed_patterns.values())}"
    )

    print("\nExample values before and after trimming:")

    for column_name in COLUMNS_TO_SAMPLE:
        if column_name not in header:
            print(f"\n{column_name}: column not found")
            continue

        index = header.index(column_name)

        if not rows:
            print(f"\n{column_name}: no valid rows to sample")
            continue

        original_value = rows[0][index]
        trimmed_value = original_value.strip()

        print(f"\n{column_name}:")
        print(f"  Original: {original_value!r}")
        print(f"  Trimmed:  {trimmed_value!r}")


def main():
    """Compare raw and trimmed row patterns in all source files."""

    print("HOTEL REVENUE & BOOKING INTELLIGENCE")
    print("Raw vs. trimmed row comparison")
    print("Original CSV files will not be modified.")

    for filename in FILES:
        compare_rows(DATA_DIR / filename)


if __name__ == "__main__":
    main()
