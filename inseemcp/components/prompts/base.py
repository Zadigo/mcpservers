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
def find_all_establishments_with_siren(siren: str) -> PromptResult:
    """
    Find all establishments associated with a given SIREN number.

    Args:
        siren (str): The SIREN number to search for.
    """
    return PromptResult(
        messages=[
            Message(
                role='user',
                content=f"Find all establishments associated with the SIREN number: {siren}"
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
def explain_column(column_name: str | None = None) -> PromptResult:
    """
    Explain a specific column in the dataset. If no column name is provided, prompt the user to specify which column they would like explained.
    
    Arguments:
        column_name (str | None): The name of the column to explain. If None, the user will be prompted to provide a column name.
    """

    messages = [
        Message(
            role='user',
            content=f"Can you explain a column in the dataset{f': {column_name}' if column_name else ''}"
        )
    ]

    if column_name is None:
        messages.append(
            Message(
                role='assistant',
                content="Which column would you like me to explain? Please provide the column name."
            )
        )

    return PromptResult(messages=messages)
