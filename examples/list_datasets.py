from __future__ import annotations

import logging

from bma_opendata import BangkokOpenDataClient, CKANApiError

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    with BangkokOpenDataClient(cache_ttl=300) as client:
        try:
            response = client.list_datasets()
        except CKANApiError as exc:
            logger.error("Failed to fetch dataset list: %s", exc)
            return

        logger.info("Found %s datasets.", len(response.result))
        for slug in response.result[:10]:
            logger.info("- %s", slug)


if __name__ == "__main__":
    main()
