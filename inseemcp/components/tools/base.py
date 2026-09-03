from fastmcp.tools import tool
from pydantic import Field


@tool
def search_single_siren(siren: str):
    """
    Search for a single SIREN number.

    Arguments:
        siren (str): The SIREN number to search for.
    """


@tool
def search_single_siret(siret: str):
    """
    Search for a single SIRET number.

    Arguments:
        siret (str): The SIRET number to search for.
    """


@tool
def search_all_siren_startswith(siren: str):
    """
    Search for all SIREN numbers that start with a specific string.

    Arguments:
        siren (str): The starting string of the SIREN numbers to search for.
    """


@tool
def search_all_businesses_with_siren(siren: str):
    """
    Search for all businesses with a specific SIREN number.

    Arguments:
        siren (str): The SIREN number of the businesses to search for.
    """


@tool
def search_all_purged_legal_units():
    """
    Search for all purged legal units.
    """


@tool
def search_all_purged_establishments():
    """
    Search for all purged establishments.
    """


@tool
def search_all_establishments_within_commune(commune_code: str):
    """
    Search for all establishments within a specific "commune". A "commune" is the smallest administrative 
    division in France, similar to a municipality or township.

    Arguments:
        commune_code (str): The code of the commune to search for establishments.
    """


@tool
def search_for_establishments_by_name(name: str):
    """
    Search for establishments with a specific name.

    Arguments:
        name (str): The name of the establishments to search for.
    """


@tool
def search_for_establishments_by_activity_code(activity_code: str = Field(description="The activity code of the establishments to search for.")):
    """
    Search for establishments with a specific activity code.

    Arguments:
        activity_code (str): The activity code of the establishments to search for.
    """


@tool
def search_for_terminated_legal_units():
    """
    Search for all terminated legal units.
    """


@tool
def search_for_establishments_where_legal_unit_is_person():
    """
    Search for all establishments where the legal unit is a person.
    """


@tool
def search_for_establishments_never_closed():
    """
    Search for all establishments that have never been closed.
    """


@tool
def multisearch():
    pass
