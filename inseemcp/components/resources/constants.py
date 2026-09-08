from typing import Any

from fastmcp import FastMCP
from fastmcp.resources import FileResource
from pydantic import AnyUrl

from utils import STATIC_DIR

RESOURCE_DEFINITIONS: list[dict[str, Any]] = [
    {
        "uri": "concepts://dataset/readme",
        "path": STATIC_DIR / "README.md",
        "name": "INSEE Dataset Overview",
        "description": (
            "Overview of the French INSEE enterprise and association "
            "datasets exposed by this MCP server."
        ),
        "category": "documentation",
    },
    {
        "uri": "concepts://dataset/concepts/siren",
        "path": STATIC_DIR / "concepts/siren.md",
        "name": "SIREN",
        "description": (
            "Definition and semantics of the 9-digit SIREN identifier "
            "for a French legal unit."
        ),
        "category": "concept",
    },
    {
        "uri": "concepts://dataset/concepts/siret",
        "path": STATIC_DIR / "concepts/siret.md",
        "name": "SIRET",
        "description": (
            "Definition and semantics of the 14-digit SIRET identifier "
            "for a French establishment."
        ),
        "category": "concept",
    },
    {
        "uri": "concepts://dataset/concepts/legal-unit",
        "path": STATIC_DIR / "concepts/legal-unit.md",
        "name": "Legal Unit",
        "description": (
            "Definition and semantics of a French legal unit identified "
            "by a SIREN."
        ),
        "category": "concept",
    },
    {
        "uri": "concepts://dataset/concepts/establishment",
        "path": STATIC_DIR / "concepts/establishment.md",
        "name": "Establishment",
        "description": (
            "Definition and semantics of an establishment identified "
            "by a SIRET."
        ),
        "category": "concept",
    },
    {
        "uri": "concepts://dataset/search/behavior",
        "path": STATIC_DIR / "search/search-behavior.md",
        "name": "Search Behavior",
        "description": (
            "Rules for exact, prefix, wildcard and multi-result searches."
        ),
        "category": "search",
    }
]


def build_resources(app: FastMCP):
    """Build and add all predefined resources to 
    the given FastMCP application."""
    for resource in RESOURCE_DEFINITIONS:
        path = resource["path"]

        if not path.is_file():
            continue

        app.add_resource(
            FileResource(
                uri=AnyUrl(resource["uri"]),
                path=path,
                name=resource["name"],
                description=resource["description"],
                mime_type="text/markdown",
                tags={"documentation", resource["category"]},
            )
        )
