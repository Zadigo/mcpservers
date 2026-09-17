from argparse import ArgumentParser

# from backend.simple_requester import LawyersRequest

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        'dataset',
        type=str,
        required=True,
        choices=['lawyers']
    )

    namespace = parser.parse_args()

    # if namespace.dataset == 'lawyers':
    #     instance = LawyersRequest()
    #     asyncio.run(instance())
