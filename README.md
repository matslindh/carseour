# carseour
Python interface to extract information from the local Project Cars API.

carseour is developed against Python 3.4+, but might run under python 2.7.

## Usage
```python
import carseour

data = carseour.fetch()
```

## Installation
`pip install carseour`


## Regenerating Interface Classes
The interface is generated from the SharedMemory.h file, available from the Project Cars developers. The most recent version should also be available through [carseour on GitHub](https://github.com/matslindh/carseour/).

Regenerating the interface file requires [CppHeaderParser](https://pypi.python.org/pypi/CppHeaderParser) and [Jinja2](https://pypi.python.org/pypi/Jinja2). Run `generate_xyz.py /path/to/SharedMemory.h outputname.py` to update the API to the current shared memory format.

## Contributing

Issues and pull requests can be submitted at [carseour on GitHub](https://github.com/matslindh/carseour/)
