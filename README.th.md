# ชุดพัฒนา Bangkok Open Data (ภาษา Python)

Python SDK สำหรับดึงข้อมูลจาก API ของdata.bangkok.go.th 

## การติดตั้ง

```bash
pip install bma-opendata

# หรือหากต้องการติดตั้งจากโค้ดในเครื่องเพื่อพัฒนา
pip install -e .
```

## การใช้งานเบื้องต้น

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

## ตัวอย่างเพิ่มเติม

ใน [`examples/`](examples/) 

```bash
uv run python -m examples.list_datasets
uv run python -m examples.search_by_format --query water --format JSON
```
