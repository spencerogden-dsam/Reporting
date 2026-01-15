#!/usr/bin/env python3
"""Generate PDF reports for each household from Orion."""

import os
import sys

from data.orion import get_client, get_households, fetch_account_products, get_household_accounts
from reports.household_report import generate_household_report


def main():
    # Get credentials from environment
    username = os.environ.get("ORION_USERNAME")
    password = os.environ.get("ORION_PASSWORD")

    if not username or not password:
        print("Error: Set ORION_USERNAME and ORION_PASSWORD environment variables")
        sys.exit(1)

    # Fetch data from Orion
    print("Connecting to Orion...")
    client = get_client(username, password)

    print("Fetching account products (Query 22220)...")
    products = fetch_account_products(client)
    print(f"Loaded {len(products)} product records")

    print("Building household list...")
    household_names = get_households(client)
    print(f"Found {len(household_names)} households")

    # Generate one PDF per household
    print("Generating PDFs...")
    for i, name in enumerate(household_names, 1):
        accounts = get_household_accounts(client, name)
        output_path = generate_household_report(name, accounts)
        print(f"  [{i}/{len(household_names)}] {output_path.name}")

    print(f"Done! Generated {len(household_names)} reports in output/")


if __name__ == "__main__":
    main()
