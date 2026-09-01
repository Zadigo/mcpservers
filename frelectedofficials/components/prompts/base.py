from fastmcp.prompts import Message, PromptResult, prompt
from fastmcp.server.context import Context


@prompt
async def ask_about_datasets(context: Context):
    """Ask about the datasets that are available on the server."""
    return PromptResult(
        messages=[
            Message(role='user', content="What are the datasets that are available for French elected officials?"),
            Message(role='assistant', content="Here are the list of datasets that are available to analyze for French elected officials:"),
        ]
    )


@prompt
async def ask_about_single_dataset(name: str, context: Context):
    """Ask about a single dataset that is available on the server."""
    return PromptResult(
        messages=[
            Message(role='user', content=f"Can you tell me about the dataset '{name}'?"),
            Message(role='assistant', content="I will describe the dataset and provide information about its contents, including the columns and their descriptions."),
        ]
    )



@prompt
async def ask_about_sources(context: Context):
    """Ask about the sources of the datasets that are available on the server."""
    return PromptResult(
        messages=[
            Message(role='user', content="What are the sources of the datasets that are available for French elected officials?"),
            Message(role='assistant', content="The datasets available for French elected officials are sourced from the official open data platform of the French government, [data.gouv.fr](https://www.data.gouv.fr/datasets/repertoire-national-des-elus-1)."),
        ]
    )

