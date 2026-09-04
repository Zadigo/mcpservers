from fastmcp.prompts import Message, PromptResult, prompt


@prompt
def find_legal_unit_from_siret(siret: str) -> PromptResult:
    """
    Identify the INSEE legal unit associated with a French SIRET.

    The SIRET should normally contain 14 digits. If the input appears
    malformed, explain the expected format instead of attempting to
    fabricate a result.

    Args:
        siret: A French SIRET identifying an establishment.
    """
    return PromptResult(
        messages=[
            Message(
                role="user",
                content=f"""
                I want to identify the legal unit associated with the French SIRET
                number "{siret}".

                Use the INSEE enterprise data.

                First determine whether the supplied value looks like a valid SIRET.
                If it is valid, look up the corresponding establishment and then
                identify its associated legal unit.

                Return a concise result containing:
                1. SIRET
                2. establishment name/address, if available
                3. SIREN
                4. legal unit name
                5. relevant status information

                If multiple records are returned, explain why and distinguish them.
                If no record is found, clearly report that no matching INSEE record
                was found.

                Do not guess or substitute a different company.
                """
            )
        ]
    )


@prompt
def find_legal_units_by_name_prefix(name: str) -> PromptResult:
    """
    Find French legal units whose name begins with the supplied prefix.

    Args:
        name: The beginning of the legal unit's name.
    """
    return PromptResult(
        messages=[
            Message(
                role="user",
                content=f"""
                Search the French INSEE enterprise data for legal units whose name
                starts with "{name}".

                Use a case-insensitive match and account for normal French name
                variations where appropriate. Return the matching legal units with,
                where available:
                - legal unit name
                - SIREN
                - legal form
                - status
                - principal activity

                If there are many matches, summarize the result and present the most
                relevant matches rather than producing an unnecessarily large response.
                Do not invent or infer legal units that are not present in the INSEE data.
                """
            )
        ]
    )
