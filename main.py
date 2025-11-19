from __future__ import annotations

import logging

from bma_opendata import BangkokOpenDataClient, CKANApiError

logger = logging.getLogger(__name__)


def main() -> None:
    """Basic demonstration that lists datasets and logs dataset resources."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    with BangkokOpenDataClient(cache_ttl=600) as client:
        try:
            dataset_ids = client.list_datasets().result
        except CKANApiError as exc:
            logger.error("Unable to list datasets: %s", exc)
            return

        if not dataset_ids:
            logger.info("No datasets are currently available.")
            return

        dataset_id = dataset_ids[0]
        try:
            dataset = client.get_dataset(name=dataset_id).result
        except CKANApiError as exc:
            logger.error("Unable to load dataset '%s': %s", dataset_id, exc)
            return

        logger.info(
            "Dataset '%s' has %s resources:", dataset.title, len(dataset.resources)
        )
        for resource in dataset.resources[:5]:
            logger.info("- %s (%s) -> %s", resource.name, resource.format, resource.url)


if __name__ == "__main__":
    main()
