# Dazbo Commons

A reusable utility library.

```text
dazbo-commons/
│
├── src/
│   └── dazbo_commons/
│       ├── __init__.py
│       └── colored_logging.py
│
├── tests/
│   ├── __init__.py
│   └── test_colored_logging.py
│
├── README.md
├── setup.py
├── setup.cfg
├── LICENSE
└── requirements.txt
```

## Coloured Logging

```python
import logging
import dazbo_commons as dc

logger_name = __name__ # or just pass in a str
logger = dc.retrieve_console_logger(logger_name)
logger.setLevel(logging.INFO) # Set threshold. E.g. INFO, DEBUG, or whatever

logger.info("Some msg") # log at info level
```