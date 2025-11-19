from __future__ import annotations

import argparse
import logging

from bma_opendata import BangkokOpenDataClient, CKANApiError

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search Bangkok datasets by keyword and optional resource format."
    )
    parser.add_argument(
        "--query",
        "-q",
        default="traffic",
        help="Full-text search query (default: %(default)s)",
    )
    parser.add_argument(
        "--format",
        "-f",
        dest="res_format",
        default="CSV",
        help="Resource format filter, e.g. CSV, JSON (default: %(default)s)",
    )
    parser.add_argument(
        "--limit",
        "-n",
        type=int,
        default=5,
        help="Number of datasets to show (default: %(default)s)",
    )
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = parse_args()
    fq = f"res_format:{args.res_format}" if args.res_format else None

    with BangkokOpenDataClient(cache_ttl=120) as client:
        try:
            response = client.search_datasets(q=args.query, fq=fq, rows=args.limit)
        except CKANApiError as exc:
            logger.error("Search failed: %s", exc)
            return

        datasets = response.result.results
        if not datasets:
            logger.info("No matching datasets were found.")
            return

        for dataset in datasets:
            logger.info("%s (%s resources)", dataset.title, len(dataset.resources))


if __name__ == "__main__":
    main()
