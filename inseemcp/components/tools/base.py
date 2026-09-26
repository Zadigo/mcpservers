# from fastmcp.dependencies import CurrentContext
# from fastmcp.server.context import Context
# from fastmcp.tools import tool


# @tool
# async def process_file(file_uri: str, ctx: Context | None = None):
#     ctx = ctx or CurrentContext()
#     await ctx.info(f"Reading file from {file_uri}")
#     content = await ctx.read_resource(file_uri)
#     for item in content.contents:
#         await ctx.info(f"Processing item: {item}")
#         item.content
