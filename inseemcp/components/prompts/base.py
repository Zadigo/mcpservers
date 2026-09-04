from fastmcp.prompts import Message, PromptResult, prompt


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
