# pyResults
A result wrapper class for Python

## Installation
The package can be installed from GitHub using Pip:
```
sudo pip3 install git+git://github.com/prottonicfusion/pyResults.git#egg=pyResults
```

## Usage
```python
from py_results import result

def increment(a):
    res = result.Result()
    if type(a) == int or type(a) == float:
        res.ok(a+1)
    else:
        res.err("Not a number!")
    return res

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
