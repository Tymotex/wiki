---
title: Python
description: Python
---

![[Knowledge/Engineering/Languages/assets/python-wallpaper.png|700]]

Python is a [[Knowledge/Engineering/Programming/Type System#Dynamic Typing|dynamically-typed]] high-level programming language whose design philosophy centres around readability and terseness. It's used frequently for data science and machine learning, backend development, scripts and CLIs.

> Code is sometimes described as *pythonic*, which just means it exploits Python's language features and design to produce something very readable and elegant.

See [[Knowledge/Engineering/Languages/Python Data Science|Python for Data Science]].

---

### Dunder Methods
TODO.

### Context Manager
`with`

TODO: see https://www.pythoncheatsheet.org/cheatsheet/context-manager.

## Virtual Environments
> Always use a virtual environment. [source](https://csguide.cs.princeton.edu/software/virtualenv)

To prevent bloating the base Python installation with project dependencies and have reproducible/portable setups, use virtual environments.
```bash
pip install virtualenv
python -m venv ./venv     # Create a virtual environment in the new folder called `venv`.
source venv/bin/activate  # Use the virtual environment's Python installation.
deactivate                # Deactivate the current virtual environment.

pip freeze > requirements.txt   # Dumps all the current dependencies into `requirements.txt`.
```

## Import and Export
- **Modules** — any Python file.
- **Packages** — directories containing `__init__.py`. A package *contains* one or multiple modules or further nested packages.

```python
import foo
```
- Searches for the `foo` module in the paths in `sys.path`.
- Creates a [module object](https://github.com/python/cpython/blob/3.9/Objects/moduleobject.c) and assigns it to the `foo` variable.

```python
import foo.bar
```
- Searches for the `foo` package in the paths in `sys.path`, and then finds the `bar` module in that package.
- Creates a module object and assigns it to the `foo` variable. 

```python
from foo import bar, baz
from a import (            # Syntax for splitting a long from-import statement into multiple lines.
    b,
    c
)
```
- Searches for `foo` in the paths in `sys.path`.
- Creates a module object and assigns it to the `foo` variable. 
- Declares and initialises variables `bar = foo.bar` and `baz = foo.baz`.
    - **Note**: if the exported binding `foo.bar` doesn't exist, then Python attempts to interpret `bar` as a submodule, so it tries `import foo.bar` as a fallback.
- Deletes the `foo` variable.

### Relative Imports
> Relative imports are generally discouraged since they're less readable, less understood, and easy to break.

All relative imports are done with `from _ import _`. The `import _` statement is always absolute.
```python
from . import foo     # From the current package, import `foo`.
from .bar import baz  # From the `bar` module in the current package, import `baz`.
```
- `.` is the *current package*, which is what `__package__` is set to.
- `..` is the parent package.

**Having trouble?**
Some crucial details to note:
- Python files are loaded as either a *module* or a *top-level script*. When you do `python app.py`, you are loading `app.py` as a top-level script.
- Top-level scripts have `__name__` set to `__main__`. There is only ever 1 top-level script.
- Modules have `__name__` set to a dot-separated string of their package path.
- The `__name__` is used to determine where the current file is in a package, **not the filesystem structure** like in other languages. If `__name__` is `__main__`, then you'll get the `no known parent package` error.

### `__init__.py`
The presence of this file (even if empty) indicates that the containing folder is a **package**, not a regular directory. This rule was dropped for subpackages, however, [to improve developer experience](https://mail.python.org/pipermail/python-dev/2006-April/064400.html).

Whatever you import inside `__init__.py` becomes accessible directly under the package name for consumers. Eg. in the example below, consumers can just do `from foo import baz`. This works a bit similarly to the `index.js` file exporting variables in JavaScript.
```python
# foo/__init__.py
from foo.bar import baz
```

## Classes

Take notes from here: https://stackoverflow.com/questions/9056957/correct-way-to-define-class-variables-in-python

To make a member private, prefix its name with an underscore `_`. This doesn't actually do anything, it's just an agreed upon standard for documenting something  should be private. There's nothing stopping users of the class from invoking private methods.
- **Name mangling** ensures that subclasses don't unknowingly override a private function with the same name.

TODO: `@classmethod` decorator. See https://stackoverflow.com/questions/54264073/what-is-the-use-and-when-to-use-classmethod-in-python

#### Getter and Setter
```python
class Foo:
    def __init__(self):
        self._foo = ""

    @property
    def foo(self):
        """ Getter. """
        return self._foo

    @foo.setter
    def foo(self, new_foo):
        """ Setter. """
        self._foo = new_foo
```

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

## Standard Built-In Modules
See [standard built-in modules](https://docs.python.org/3/py-modindex.html).

### File Manipulation
Python has built-in top-level functions for file manipulation:
```python
# Reading.
my_file = open(filename, "r")
lines: List[str] = my_file.readlines()
my_file.close()

# Alternatively, using `with`:
with open(filename, "r") as my_file:
    lines: List[str] = my_file.readlines()

# Writing.
with open(filename, "w") as my_file:
    my_file.write("Hi.")
```

### OS
[`os`](https://docs.python.org/3/library/os.html) provides a bunch of useful functions for working with the filesystem.
```python
os.getcwd()
os.path.exists(path)
os.path.isdir(path)
os.path.join(*path_fragments)   # Forms a complete path in a cross-OS way (since Windows uses backslash separators).
os.makedirs(path)                 # Like `mkdir -p`, which creates all non-existent directories along the path.
```

### Regex
See [[Knowledge/Engineering/Languages/Regex|regex]].

> Use raw strings `r"..."` when specifying regex patterns to avoid being confused about what characters are being escaped.

```python
regex = re.compile(r"...")
match = regex.search(haystack)  # `re.Match` object contains info about the search. If no match was found, then `match == None`.

# Equivalent to the above, but you can't reuse the compiled regex.
result = re.match(r"...", haystack)
```

**Capture Groups**:
```python
match = re.match(r"(\w+) (\w+)", "Linus Torvalds")

match[0]        # The original string, "Linus Torvalds".
match.group(0)  #   Equivalent to above.

match[1]        # First capture group, "Linus".
match.group(1)  #   Equivalent to above.

match[2]        # Second capture group, "Torvalds".
match.group(2)  #   Equivalent to above.
```

### Dates
Use [`datetime`](https://docs.python.org/3/library/datetime.html) to work with dates. Use [`time`](https://docs.python.org/3/library/time.html) for lower-level operations involving time.

**Convert between strings and dates**:
```python
from datetime import datetime

# strptime: str → datetime
date_str = "2022-09-20"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

# strftime: datetime → str
date_obj = datetime.now()
date_str = date_obj.strftime("%Y-%m-%d")
```

**Date arithmetic and comparison**:
Use `timedelta` to add/subtract time from a date. You can directly use comparison operators on `datetime` objects.
```python
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)

assert(yesterday < today)
```
