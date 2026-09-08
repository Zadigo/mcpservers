import json

from fastmcp.resources import ResourceResult, resource
from pydantic import AnyUrl

from components.resources.constants import RESOURCE_DEFINITIONS
from utils import STATIC_DIR


@resource("folder://{folder_name}")
async def browse_workspace_directory(folder_name: str) -> ResourceResult:
    """Dynamically browse and list files within a requested workspace folder."""
    
    target_path = STATIC_DIR.joinpath(folder_name).resolve()
    
    if not target_path.is_relative_to(STATIC_DIR):
        raise ValueError("Access Denied: Attempted to escape workspace root.")
        
    if not target_path.exists() or not target_path.is_dir():
        raise ValueError(f"Directory not found: {folder_name}")

    from fastmcp.resources import DirectoryResource

    dir_resource = DirectoryResource(
        path=target_path,
        uri=AnyUrl(f"folder://{folder_name}")
    )
    
    return await dir_resource.read()


@resource("concepts://dataset/manifest")
def dataset_manifest() -> str:
    manifest = {
        "name": "INSEE Dataset",
        "description": (
            "Semantic index of the documentation and concepts "
            "available through this MCP server."
        ),
        "identifiers": {
            "SIREN": {
                "description": "Identifies a legal unit.",
                "length": 9,
                "resource": "concepts://dataset/concepts/siren",
            },
            "SIRET": {
                "description": "Identifies an establishment.",
                "length": 14,
                "resource": "concepts://dataset/concepts/siret",
            },
        },
        "relationships": [
            {
                "from": "SIREN",
                "to": "SIRET",
                "relationship": (
                    "A legal unit identified by a SIREN can have "
                    "one or more establishments identified by SIRETs."
                ),
            }
        ],
        "resources": [
            {
                "uri": resource["uri"],
                "name": resource["name"],
                "description": resource["description"],
                "category": resource["category"],
            }
            for resource in RESOURCE_DEFINITIONS
                if resource["path"].is_file()
        ]
    }

    return json.dumps(manifest, ensure_ascii=False, indent=2)
