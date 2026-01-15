"""Orion data fetching utilities."""

from orionapi import OrionAPI

# Query ID for all products in all accounts
ACCOUNT_PRODUCTS_QUERY_ID = 22220

# Module-level cache for query data
_account_products_data: list[dict] | None = None


def get_client(username: str, password: str) -> OrionAPI:
    """Create and return an authenticated Orion API client."""
    return OrionAPI(usr=username, pwd=password)


def fetch_account_products(client: OrionAPI) -> list[dict]:
    """Fetch all products in all accounts from Orion Query 22220.

    This query contains every product owned in every account, which can be
    used to sum up by household or account.

    Returns a list of product records. Results are cached at module level.
    """
    global _account_products_data

    if _account_products_data is not None:
        return _account_products_data

    response = client.query(ACCOUNT_PRODUCTS_QUERY_ID)
    _account_products_data = response
    return _account_products_data


def get_households(client: OrionAPI) -> list[str]:
    """Get unique list of household names from account products data.

    Returns a sorted list of unique household names.
    """
    data = fetch_account_products(client)

    # Extract unique household names
    household_names = set()
    for record in data:
        household_name = record.get("household Name")
        if household_name:
            household_names.add(household_name)

    return sorted(household_names)


def get_household_data(client: OrionAPI, household_name: str) -> list[dict]:
    """Get all account product records for a specific household.

    Args:
        client: Authenticated Orion API client
        household_name: Name of the household to filter by

    Returns:
        List of product records belonging to the household
    """
    data = fetch_account_products(client)
    return [r for r in data if r.get("household Name") == household_name]


def get_household_accounts(client: OrionAPI, household_name: str) -> list[dict]:
    """Get unique accounts for a household, sorted by balance descending.

    Args:
        client: Authenticated Orion API client
        household_name: Name of the household

    Returns:
        List of account dicts with keys: name, type, balance
        Sorted by balance descending (largest first)
    """
    records = get_household_data(client, household_name)

    # Deduplicate by account ID
    accounts_by_id = {}
    for record in records:
        account_id = record.get("account ID")
        if account_id and account_id not in accounts_by_id:
            accounts_by_id[account_id] = {
                "name": record.get("reg Name", ""),
                "type": record.get("reg Description", ""),
                "balance": record.get("accountValue", 0) or 0,
            }

    # Sort by balance descending
    accounts = sorted(accounts_by_id.values(), key=lambda a: a["balance"], reverse=True)
    return accounts
