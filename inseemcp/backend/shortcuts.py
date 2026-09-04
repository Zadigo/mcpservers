from typing import Any

from backend.base import AbstractRequester


async def query(requester: AbstractRequester, testing: bool = False) -> dict[str, Any]:
    """Function that takes an AbstractRequester instance and sends a request to the Api
    using the request_builder method of the AbstractRequester class. It returns the response
    from the Api as a dictionary
    
    .. code-block:: python

        from backend import SearchEstablishment, query

        instance = SearchEstablishment()
        response = await query(instance)
        print(response)
    """
    instance = requester.request_builder()
    return await instance.send_request(instance.get_url(), testing=testing)
