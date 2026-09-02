import asyncio
from argparse import ArgumentParser

from utils import logger

if __name__ == "__main__":
    from utils import FilesQueryset

    parser = ArgumentParser(description="Prefetch files from the source directory and cache them in Redis.")
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit the number of files to prefetch. If not provided, all files will be prefetched.",
    )
    parser.add_argument(
        "--clean-cache",
        action="store_true",
        help="Clear the cache before prefetching files.",
    )
    args = parser.parse_args()

    logger.info("Starting prefetching files...")

    instance = FilesQueryset()
    asyncio.run(instance.prefetch_files(limit=args.limit, clean_cache=args.clean_cache))
