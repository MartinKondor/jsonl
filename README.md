# jsonl

[![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg)](https://github.com/MartinKondor/jsonl/)
[![version](https://img.shields.io/badge/version-2023.11-brightgreen.svg)](https://github.com/MartinKondor/jsonl)
[![GitHub Issues](https://img.shields.io/github/issues/MartinKondor/jsonl.svg)](https://github.com/MartinKondor/jsonl/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-blue.svg)

Utilities for using JSONL (JSON lines) file type with Python.

## Getting Started

### Prerequisites

* Python 3.6+
* Python modules from the `requirements.txt`

### Deployment

Dowload and install the dependencies with the command:

```
$ python -m pip install -r requirements.txt
```

## Usage

Install the module.
```bash
pip install git+https://github.com/MartinKondor/jsonl.git
```

Import and define a list of objects to work with.
```python
from typing import List, Any
from jsonl import jsonl


a: List[Any] = [
    {"first_name": "Joe1", "last_name": "Doe1"},
    {"first_name": "Joe2", "last_name": "Doe2"},
    {"first_name": "Joe3", "last_name": "Doe3"},
]
```

Save the object to a file:
```python
jsonl.dump(a, "dummy_data.jsonl")
```

Append an object to a file (works even if the file didn't exist).
```python
obj: Any = {"first_name": "Joe_Appended", "last_name": "Doe_Appended"}
jsonl.append(obj, "dummy_data.jsonl")
```

Load the jsonl file's data:
```python
data = jsonl.load("dummy_data.jsonl")
```

Print out the JSON object nicely:
```python
jsonl.print(data)
```

## Contributing

This project is open for any kind of contribution from anyone.

### Steps

1. Fork this repository
2. Create a new branch (optional)
3. Clone it
4. Make your changes
5. Upload them
6. Make a pull request here

## Authors

* **[Martin Kondor](https://MartinKondor.github.io/)**

# License

Copyright (C) 2023-2024 Martin Kondor.

See the [LICENSE](LICENSE) file for details.
