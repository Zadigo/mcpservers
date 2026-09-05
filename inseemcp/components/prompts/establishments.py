import datetime

from fastmcp.prompts import Message, PromptResult, prompt


@prompt
def find_establishments_by_siren(siren: str) -> PromptResult:
    """
    Find all French establishments belonging to the legal unit identified
    by a SIREN.

    Args:
        siren: A 9-digit French SIREN identifying a legal unit.
    """
    return PromptResult(
        messages=[
            Message(
                role="user",
                content=f"""
                Using the French INSEE enterprise data, find the legal unit identified
                by SIREN "{siren}" and list the establishments associated with it.

                Remember that a SIREN identifies a legal unit, while a SIRET identifies
                an individual establishment belonging to that legal unit.

                For each establishment, provide, where available:
                - SIRET
                - establishment name
                - address
                - establishment status
                - principal activity

                Also provide the legal unit's name and SIREN.

                If the SIREN is invalid or no matching legal unit is found, report that
                clearly. Do not guess or substitute a different SIREN.
                """
            )
        ]
    )


@prompt
def find_establishments_by_siren_prefix(siren_prefix: str) -> PromptResult:
    """
    Find French establishments whose associated SIREN begins with a
    specified prefix.

    Args:
        siren_prefix: The beginning of a SIREN.
    """
    return PromptResult(
        messages=[
            Message(
                role="user",
                content=f"""
                Search the French INSEE enterprise data for establishments whose
                associated SIREN starts with "{siren_prefix}".

                Treat the supplied value as a SIREN prefix, not as a complete SIREN.

                For each matching establishment, provide, where available:
                - SIRET
                - SIREN
                - establishment name
                - address
                - establishment status
                - principal activity

                If the prefix is empty, malformed, or produces a very large number of
                matches, explain the issue and summarize the results rather than
                returning an unnecessarily large list.

                Only report establishments present in the INSEE data.
                """
            )
        ]
    )


@prompt
def find_establishments_excluding_siren_prefix(
    siren_prefix: str,
) -> PromptResult:
    """
    Find French establishments whose associated SIREN does not begin
    with the specified prefix.

    Args:
        siren_prefix: A SIREN prefix to exclude from the search.
    """
    return PromptResult(
        messages=[
            Message(
                role="user",
                content=f"""
                Using the French INSEE enterprise data, find establishments whose
                associated SIREN does NOT start with "{siren_prefix}".

                Treat "{siren_prefix}" as a SIREN prefix to exclude.

                Because this condition may match a very large number of establishments,
                do not attempt to return an unbounded list. Instead:
                - apply the exclusion condition to the INSEE data;
                - report the number of matching records when available;
                - return a representative or limited set of results;
                - explain any result limit or pagination.
                - ensure pagination is no more than 20 records

                For returned establishments, provide, where available:
                - SIRET
                - SIREN
                - establishment name
                - address
                - establishment status
                - principal activity

                If the prefix is invalid or empty, explain the problem rather than
                performing an unrestricted search.

                Finally, if the total number of records if over a 1000 explain briefly
                the the total amount of results and total amount of pages needed to
                explore the rest of the data.
                """
            )
        ]
    )


@prompt
def find_enterprise_by_activity(code_actvity: str, location: str = '*') -> PromptResult:
    d = datetime.datetime.now(tz=datetime.UTC)

    current_year = d.year
    previous_year = current_year - 1

    return PromptResult(
        messages=[
            Message(
                role='user',
                content=f"""
                I want to get a list of enterprises that are officially registered in the
                INSEE dataset that match the similar code activity (code NAF or APE) as mines 
                which is {code_actvity}.

                The NAF/APE must be a 5 carachter long value that ends with a letter. For example
                91.01Z or 66.11Z.

                Remember that the NAF/APE can be described as followed. Using the following code 47.11C as an example:

                - Section: G – Wholesale and retail trade; repair of motor vehicles and motorcycles
                - Division 47 – Retail trade, except of motor vehicles and motorcycles
                - Group: 47.1 – Retail sale in non-specialized stores
                - Class: 47.11 – Retail sale in non-specialized stores with food, beverages or tobacco predominating
                _ Subclass: 47.11C – Convenience stores / Mini-markets (Supérettes)

                You MUST match in priority businesses that in the first two-digit division as mines for instance, taking the
                exapmple above, the businesses should strictily match the 47 division.
                
                An small exapnsion can be made using the group to match similar business (e.g. 47.1) that are are in the same
                perimeter as mines.

                Provide a summary on your findings and how closely are they related to mines. Finally, focus on results that
                are between {current_year} and {previous_year} unless specified otherwise. If the the location value "{location}", 
                which is a xxxx department area in France, is "*" search in all of France, otherwise, focus on the area that 
                was provided.
                """
            )
        ]
    )
