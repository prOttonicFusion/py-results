# py-results
A result wrapper class for Python

## Installation
The package can be installed from GitHub using Pip:
```sh
pip install git+https://github.com/prottonicfusion/py-results.git

# or for a specific version
pip install git+https://github.com/prottonicfusion/py-results.git@v1.0.0
```

## Usage
```python
from py_results import Result, Ok, Err

def increment(a) -> Result[int]:
    if type(a) == int or type(a) == float:
        return Ok(a+1)
    return Err("Not a number!")

res = increment(sys.argv[1])

if res.is_ok():
    print("The incremented result is: ", res.unwrap())
else:
    print("Error: ", res.unwrap())
```

## Development

### Testing
The provided unit tests can be run using:
```
python3 -m unittest
```

### Building
To build the package and create the distribution package, run
```
python3 setup.py sdist
```
from the projct root.
