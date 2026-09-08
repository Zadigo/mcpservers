from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        'dataset',
        type=str,
        required=True,
        choice=['lawyers']
    )

    namespace = parser.parse_args()

    # if namespace.dataset == 'lawyers':
    #     instance = LawyersRequest()
    #     asyncio.run(instance())
