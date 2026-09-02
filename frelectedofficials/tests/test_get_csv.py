import asyncio

import pytest

from endpoints import ConcreteDistrictCouncillor, generate_elected_officials


@pytest.mark.parametrize(
    'klass', 
    [
        ConcreteDistrictCouncillor,
    ]
)
async def test_generate_elected_officials(klass):
    result = await generate_elected_officials(klass())
    
    assert result is not None
    assert not result.empty

    # Test cache
    result = await generate_elected_officials(klass())
    assert result is not None



async def test_elected_officials_fetch_csv(elected_officials):
    result = await elected_officials.fetch_csv_file()
    assert result is not None  


async def test_fetch_cache_or_csv(elected_officials):
    result = await elected_officials.fetch_cache_or_csv(force_clear_cache=True)
    assert result is not None  


ENDPOINTS = pytest.mark.parametrize(
    'title,url,filename',
    [
        (
            "Élus conseiller d'arrondissement (CA)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-154541/elus-conseiller-darrondissement-ca.csv',
            'elus-conseiller-darrondissement-ca.csv'
        ),
        (
            "Élus conseiller municipal (CM)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-154802/elus-conseiller-municipal-cm.csv',
            'elus-conseiller-municipal-cm.csv',
        ),
        (
            "Élus conseiller communautaire (EPCI)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-154854/elus-conseiller-communautaire-epci.csv',
            'elus-conseiller-communautaire-epci.csv',
        ),
        (
            "Élus conseiller départemental (CD)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-154909/elus-conseiller-departemental-cd.csv',
            'elus-conseiller-departemental-cd.csv',
        ),
        (
            "Élus conseiller régional (CR)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-154932/elus-conseiller-regional-cr.csv',
            'elus-conseiller-regional-cr.csv',
        ),
        (
            "Élus membre d'une assemblée (MA)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-154945/elus-membre-dune-assemblee-ma.csv',
            'elus-membre-dune-assemblee-ma.csv',
        ),
        (
            "Élus représentant au parlement européen (RPE)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-155000/elus-representant-parlement-europeen-rpe.csv',
            'elus-representant-parlement-europeen-rpe.csv',
        ),
        (
            "Élus sénateur (SEN)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-155016/elus-senateur-sen.csv',
            'elus-senateur-sen.csv',
        ),
        (
            "Élus député (DEP)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-155035/elus-depute-dep.csv',
            'elus-depute-dep.csv',
        ),
        (
            "Élus maire (MAI)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260811-155100/elus-maire-mai.csv',
            'elus-maire-mai.csv',
        ),
        (
            "Élus conseillers des Français de l'étranger (CONS)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260505-152134/elus-conseillers-des-francais-de-letranger-cons.csv',
            'elus-conseillers-des-francais-de-letranger-cons.csv',
        ),
        (
            "Élus assemblée des Français de l'étranger (AFE)",
            'https://static.data.gouv.fr/resources/repertoire-national-des-elus-1/20260505-152148/elus-assemblee-des-francais-de-letranger-afe.csv',
            'elus-assemblee-des-francais-de-letranger-afe.csv',
        )
    ]
)

@ENDPOINTS
async def test_api_endpoints_with_cache(elected_officials, title, url, filename):
    elected_officials.title = title
    elected_officials.url = url
    elected_officials.filename = filename

    result = await elected_officials.fetch_csv_file(fetch_only=False, no_fix=False, cache_url=True)
    await asyncio.sleep(1)  # Allow some time for the cache to be set
    assert result is not None


@ENDPOINTS
async def test_api_endpoints_no_cache(elected_officials, title, url, filename):
    # This test ensures that the elected officials class can fetch the CSV 
    # file without using the cache and that the data is processed correctly since
    # on certain endpoints the csv content raises an error  when fixing the data
    elected_officials.title = title
    elected_officials.url = url
    elected_officials.filename = filename

    result = await elected_officials.fetch_csv_file(no_fix=False)
    await asyncio.sleep(1)  # Allow some time for the cache to be set
    assert result is not None


@ENDPOINTS
async def test_api_endpoints_no_fix(elected_officials, title, url, filename):
    elected_officials.title = title
    elected_officials.url = url
    elected_officials.filename = filename

    result = await elected_officials.fetch_csv_file(no_fix=True)
    await asyncio.sleep(1)  # Allow some time for the cache to be set
    assert result is not None
