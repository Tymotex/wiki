---
title: Python
description: Python
---




### Dunder Methods
TODO.


## Virtual Environments

```bash
python3 -m venv ./venv    # Create a virtual environment 
```


Basic python installation
```
```

## Import and Export
- **Modules** — any Python file.
- **Packages** — directories containing `__init__.py`. A package *contains* one or multiple modules or further nested packages.

```python
import mod
```
This does the following:
- Searches for the `mod` module in the paths in `sys.path`.
- Creates a [module object](https://github.com/python/cpython/blob/3.9/Objects/moduleobject.c).
- Assigns it to the `mod` variable.


- You can wrap imports in parentheses.
    ```python
    from foo import (
        bar,
        baz
    )
    ```

## Classes

Take notes from here: https://stackoverflow.com/questions/9056957/correct-way-to-define-class-variables-in-python

To make a member private, prefix its name with an underscore `_`. This doesn't actually do anything, it's just an agreed upon standard for documenting something  should be private. There's nothing stopping users of the class from invoking private methods.
- **Name mangling** ensures that subclasses don't unknowingly override a private function with the same name.

TODO: `@classmethod` decorator. See https://stackoverflow.com/questions/54264073/what-is-the-use-and-when-to-use-classmethod-in-python

## Type System
Python is [[Knowledge/Engineering/Programming/Type System#Dynamic Typing|dynamically-typed]] and [will always stay that way](https://peps.python.org/pep-0484/#non-goals), however you can still opt to add static types wherever you find it useful, like how you might mix JavaScript and TypeScript code. Static typing is massively helpful in large projects as opposed to one-off scripts.

### Type Hints
> Type hints **do nothing** at runtime. You have to use a static type checker such as [Mypy](https://realpython.com/python-type-checking/), or [PyLance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) with VSCode, for example.

Typing variables and functions in Python is very similar to [[Knowledge/Engineering/Languages/TypeScript#Functions|how it's done in TypeScript]]. 
```python
def make_greeting(name: str, age: int = 42) -> str:
    return f"{name} {age}"

greeting: str = make_greeting("Andrew")    # Although the type can be inferred, annotating the type is still great for documentation.
print(greeting)
```

### typing Module
Python 3.5 supplies the [`typing`](https://docs.python.org/3/library/typing.html) built-in module brings in a lot of advanced static typing utilities such as those seen in TypeScript. 

---
