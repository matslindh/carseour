# carseour
Python interface to extract information from the local Project Cars API.

carseour is developed against Python 3.4+, but might run under python 2.7.

carseour is licensed under the MIT license (see [LICENSE](https://github.com/matslindh/carseour/blob/master/LICENSE)).

## Usage
Shared Memory must be activated in Project Cars by setting the "User Shared Memory" option under Options / Visuals / Hardware to YES.

```python
import carseour

# get a live view of the game - this is backed straight from the game's memory, and is updated for each rendered frame
game = carseour.live()

# get a snapshot of the state of the game - this reads the memory and copies it before returning the object.
game = carseour.snapshot()

# print current speed of vehicle
print(game.mSpeed)
```

All properties following the .mProperty naming scheme are internal values mapped into the python module. Other
properties are named appropriately.

## Installation

You can either install the zipball from github, or let `pip` use git itself:

`pip install https://github.com/matslindh/carseour/zipball/master`

or

`pip install git+git://github.com/matslindh/carseour.git`

## Regenerating Interface Classes
The interface is generated from the SharedMemory.h file, available from the Project Cars developers. The most recent
version should also be available at the GitHub repository for the library [carseour on GitHub](https://github.com/matslindh/carseour/).

Regenerating the interface file requires [CppHeaderParser](https://pypi.python.org/pypi/CppHeaderParser) and
[Jinja2](https://pypi.python.org/pypi/Jinja2). Run `python bin/generate_classes.py` to update the API to the current
shared memory format described in `etc/SharedMemory.h`.

## Contributing

Issues and pull requests can be submitted at [carseour on GitHub](https://github.com/matslindh/carseour/)
