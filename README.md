# nanobind-poetry-demo
Proof that I can use poetry with nanobind to call C++ from Python

## Build
Open this repo in PyCharm, setting up a local virtual environment with python 3.10.+ as the interpreter. Then, build and install the wheel...

`
python -m pip install .
`

If you make changes to the C++ code, re-run this command.

## Run a Demo
`
python nanobind_poetry_demo/say_hi.py
`

## Run Tests
`
python -m pytest tests
`

## Run Interactively
In a python console, run python code that invokes the nanobind C++ extension like this...

```
>>> from nanobind_poetry_demo.say_hi import say_hi
>>> say_hi()
numpy (poetry dependency) says pi = 3.141592653589793
hello_ext (c++ via nanobind) says hi... Whassup, sucka?
```

Or, just run code from the C++ extension directly...
```
>>> import hello
>>> print(hello.hello())
Whassup, sucka?
```


## Troubleshoot

If the build instructions didn't work immediately, open a terminal (from within your IDE, if applicable) and check that the command line prompt is prefixed by the local virtual environment name...
```
(.venv) frymire@xps17:~/code/nanobind-poetry-demo$
```
We see `(.venv)` in this case. If not, call `source .venv/bin/active` or the equivalent to activate your local virtual environment.
