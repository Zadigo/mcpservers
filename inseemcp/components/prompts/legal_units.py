from fastmcp.prompts import Message, PromptResult, prompt


@prompt
def find_legal_unit_with_siret_number(siret: str) -> PromptResult:
    """
    Find the legal unit associated with a given SIRET number.    

    Args:
        siret (str): The SIRET number to search for.
    """
    return PromptResult(
        messages=[
            Message(
                role='user',
                content=f"Find the legal unit with the SIRET number: {siret}"
            )
        ]
    )


@prompt
def find_legal_unit_name_startswith(name: str) -> PromptResult:
    """
    Find all legal units whose name starts with the given prefix.

    Args:
        name (str): The name prefix to search for.
    """
    return PromptResult(
        messages=[
            Message(
                role='user',
                content=f"Find all legal units whose name starts with the prefix: {name}"
            )
        ]
    )
