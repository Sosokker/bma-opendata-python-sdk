# Bangkok Open Data Python SDK

Lightweight wrapper around the Bangkok CKAN Action API with typed models, caching, and friendly error handling.

## Installation

```bash
pip install -e .
```

## Usage

```python
import logging
from bma_opendata import BangkokOpenDataClient

logging.basicConfig(level=logging.INFO)

with BangkokOpenDataClient() as client:
    ids = client.list_datasets().result
    if ids:
        dataset = client.get_dataset(name=ids[0]).result
        logging.info("Dataset %s has %s resources", dataset.title, len(dataset.resources))
```
