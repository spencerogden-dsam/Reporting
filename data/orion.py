"""Orion data fetching utilities."""

from orionapi import OrionAPI


def get_client(username: str, password: str) -> OrionAPI:
    """Create and return an authenticated Orion API client."""
    return OrionAPI(usr=username, pwd=password)


def get_households(client: OrionAPI) -> list[dict]:
    """Fetch all households from Orion.

    Returns a list of household dictionaries with at minimum 'id' and 'name' keys.
    """
    response = client.api_request(f"{client.base_url}/Household/Households")
    return response.json()
