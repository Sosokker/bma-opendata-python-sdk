# Bangkok Open Data Python SDK

[![CI](https://github.com/Sosokker/bma-opendata-python-sdk/actions/workflows/workflow.yml/badge.svg)](https://github.com/Sosokker/bma-opendata-python-sdk/actions/workflows/workflow.yml)

[ไทย](README.th.md).

---

Lightweight wrapper around the Bangkok CKAN Action API with typed models, caching, and friendly error handling.

## Installation

```bash
pip install bma-opendata

# or install from a local checkout for development
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

## Examples

Additional runnable examples live under [`examples/`](examples/) and cover listing datasets and searching with filters.
Run them with your preferred tool, e.g.:

```bash
uv run python -m examples.list_datasets
uv run python -m examples.search_by_format --query water --format JSON
```
