from fastmcp.prompts import Message, PromptResult


def find_association_by_postal_code(postal_code: str):
    """
    Find associations by postal code.

    Args:
        postal_code (str): The postal code to search for associations.

    Returns:
        PromptResult: A prompt result containing the user's query message.
    """
    return PromptResult(
        messages=[
            Message(
                role="user",
                content=f"""
                Search the Répertoire National des Associations for associations located 
                in the postal code: {postal_code}.

                Use a case-insensitive match and account for normal French name
                variations where appropriate.

                In case of multiple matches, summarize the results and propose the most
                relevant associations instead of producing large results.

                Do not invent or infer associations that are not present in the data.

                For your summary, focus primarily on these fields:
                * Association name
                * Short title
                * Object (or the reason for the association)
                * Postal code (adrs_codepostal)
                """
            )
        ]
    )


def find_associations_by_activity(activity: str) -> PromptResult:
    """
    Find French associations whose declared purpose or activity matches
    a specified area.

    Args:
        activity: The activity, purpose, or field for which associations
            should be searched.

    Returns:
        A prompt instructing the assistant to search for associations
        related to the specified activity.
    """
    return PromptResult(
        messages=[
            Message(
                role="user",
                content=f"""
                Find French associations whose declared purpose or activity is related
                to "{activity}".

                Search the available association data and return the most relevant
                matching associations.

                For each result, provide, where available:
                - association name
                - RNA identifier
                - SIREN, if available
                - location
                - declared purpose or activity
                - association status

                If there are many matches, prioritize the most relevant results and
                briefly explain the basis for the match.

                Do not infer that an association performs an activity unless this is
                supported by the available association data.
                """
            )
        ]
    )
