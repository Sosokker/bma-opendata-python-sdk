from __future__ import annotations

from bma_opendata import BangkokOpenDataClient, CKANApiError


def main() -> None:
    """Basic demonstration that lists datasets and prints the first dataset's resources."""

    with BangkokOpenDataClient(cache_ttl=600) as client:
        try:
            dataset_ids = client.list_datasets().result
        except CKANApiError as exc:
            print(f"Unable to list datasets: {exc}")
            return

        if not dataset_ids:
            print("No datasets are currently available.")
            return

        dataset_id = dataset_ids[0]
        try:
            dataset = client.get_dataset(name=dataset_id).result
        except CKANApiError as exc:
            print(f"Unable to load dataset '{dataset_id}': {exc}")
            return

        print(f"Dataset '{dataset.title}' has {len(dataset.resources)} resources:")
        for resource in dataset.resources[:5]:
            print(f"- {resource.name} ({resource.format}) -> {resource.url}")


if __name__ == "__main__":
    main()
