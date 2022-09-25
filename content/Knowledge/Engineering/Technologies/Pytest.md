---
title: Pytest
---

Pytest is a very popular and simple testing framework for running unit tests, integration tests and e2e tests in [[Knowledge/Engineering/Languages/Python|Python]] projects.

## Usage
The convention is to make a separate `tests` directory in your project root directory, then make test files with the name `test_*.py`. Inside these files, you just define functions and directly make assertions with the built-in Python `assert`. That's it (for simple tests).

```python
def test_foo():
    assert(do_foo() == ...)
```

### Exceptions Tests
To test that a function correctly raises an exception, use `with pytest.raises(ExceptionClassName)`:
```python
import pytest

def test_foo_raises_bar():
    with pytest.raises(BarException):
        # If this doesn't raise a `BarException`, then the test is considered to have failed.
        do_foo()   
```
