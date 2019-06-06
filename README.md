# pascua

[![PyPI](https://img.shields.io/pypi/v/pascua.svg)](https://pypi.org/project/pascua)
[![Read the Docs](https://img.shields.io/readthedocs/pascua.svg)](https://pascua.readthedocs.io/)
[![Travis (.org) branch](https://img.shields.io/travis/garciparedes/pascua/master.svg)](https://travis-ci.org/garciparedes/pascua/branches)
[![Coveralls github](https://img.shields.io/coveralls/github/garciparedes/pascua.svg)](https://coveralls.io/github/garciparedes/pascua)
[![GitHub](https://img.shields.io/github/license/garciparedes/pascua.svg)](https://github.com/garciparedes/pascua/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/garciparedes/pascua.svg)](https://github.com/garciparedes/pascua)

## Description 

Python library to perform code execution in fully isolated environments.

**IMPORTANT**: This repository is in the early stage of development, so its not recommended to be used yet. Nevertheless, contributions are welcome!


## Installation

You can install the latest ``pascua`` version via ``pip``:

```bash
pip install pascua
```

## How it works?

`pascua` allow us to perform code executions in isolated environments through containerization techniques. The main idea is that `pascua` builds a `docker` image with the given parameters defined in the corresponding implementation of the `Environment` constructor. 

When a call to `exec(.)` method is performed, it uses the generated `docker` image as the base in which it launches the proper interpreter or code compilation to execute the given `source_code` in combination with the variables defined in the `context` dictionary.

## Usage

### Python Environment

```python
import pascua as psc

context = {
    'size': 100,
}

source_code = [
    'import numpy as np',
    'random_numbers = np.random.uniform(size=size)',
]

env = psc.PythonEnvironment(
    version='3.7.3', 
    dependencies=[
        'numpy>=1.14.0',
    ]
)

result = env.exec(source_code, context)
```

### R Environment

```python
import pascua as psc

context = {
    'size': 100,
}

source_code = [
    'random_numbers <- runif(n = size)',
]

env = psc.REnvironment(
    version='latest',
)

result = env.exec(source_code, context)
```

### C++ Environment

```python
import pascua as psc

context = {
    'size': 100,
}

source_code = [
    'float r;',
    'vector<float> random_numbers;',
    'for (int i = 0; i < size; i++) {',
    '  r = static_cast <float> (rand()) / static_cast <float> (RAND_MAX);',
    '  random_numbers.push_back(r);',
    '}',
]

env = psc.CCEnvironment(
    version='latest',
    includes=[
        'vector',
        'numeric',
    ]
)

result = env.exec(source_code, context)
```


## Development

You can install it simply typing:

```bash
python setup.py install
```

To run the tests perform:

```bash
python -m unittest discover tests
```

## License

- This project is licensed under **[MIT license](http://opensource.org/licenses/mit-license.php)**.
