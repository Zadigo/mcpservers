from models.base import FileInfo, RegistryInfo


async def test_create_file():
    registry = RegistryInfo(
        count=1, 
        files=[
            FileInfo(
                title="Élus Conseiller d'Arrondissement",
                filepath="/path/to/elus-conseiller-darrondissement-ca.csv",
                created_on="2024-06-15T12:00:00Z"
            )
        ]
    )

    await registry.create_file()
    
    assert registry.count == 1
    assert len(registry.files) == 1
    assert registry.files[0].title == "Élus Conseiller d'Arrondissement"

    registry.add_file(
        FileInfo(
            title="Élus Conseiller d'Arrondissement",
            filepath="/path/to/elus-conseiller-darrondissement-ca.csv",
            created_on="2024-06-15T12:00:00Z"
        )
    )

    assert registry.count == 2
    assert len(registry.files) == 2
