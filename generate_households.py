#!/usr/bin/env python3
"""Generate a PDF report with one page per household from Orion."""

import os
import sys

from data.orion import get_client, get_households
from reports.household_report import generate_household_pages


def main():
    # Get credentials from environment
    username = os.environ.get("ORION_USERNAME")
    password = os.environ.get("ORION_PASSWORD")

    if not username or not password:
        print("Error: Set ORION_USERNAME and ORION_PASSWORD environment variables")
        sys.exit(1)

    # Fetch households from Orion
    print("Connecting to Orion...")
    client = get_client(username, password)

    print("Fetching households...")
    households = get_households(client)
    print(f"Found {len(households)} households")

    # Generate PDF
    print("Generating PDF...")
    output_path = generate_household_pages(households)

    print(f"Done! Output: {output_path}")


if __name__ == "__main__":
    main()
