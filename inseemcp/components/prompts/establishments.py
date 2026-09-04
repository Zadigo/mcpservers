from fastmcp.prompts import Message, PromptResult, prompt


@prompt
def find_establishment_with_siren_number(siren: str) -> PromptResult:
    """
    Find the establishment associated with a given SIREN number.    

    Args:
        siren (str): The SIREN number to search for.
    """
    return PromptResult(
        messages=[
            Message(
                role='user',
                content=f"Find the establishment with the SIREN number: {siren}"
            )
        ]
    )


@prompt
def find_all_establishments_starting_with_siren(siren: str) -> PromptResult:
    """
    Find all establishments whose SIREN number starts with the given prefix.

    Args:
        siren (str): The SIREN number prefix to search for.
    """
    return PromptResult(
        messages=[
            Message(
                role='user',
                content=f"Find all establishments whose SIREN number starts with the prefix: {siren}"
            )
        ]
    )


@prompt
def find_all_establishments_siren_not_match(siren: str) -> PromptResult:
    """
    Find all establishments whose SIREN number does not match the given prefix.

    Args:
        siren (str): The SIREN number prefix that should not match.
    """
    return PromptResult(
        messages=[
            Message(
                role='user',
                content=f"Find all establishments whose SIREN number does not start with the prefix: {siren}"
            )
        ]
    )
