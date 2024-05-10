# nanobind-poetry-demo
Proof that I can use poetry with nanobind to call C++ from Python

## Build
Open this repo in PyCharm, setting up a poetry environment with python 3.10.+ as the interpreter. As a result, it should automatically pull dependencies and build the nanobind C++ extension. 

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

## Rebuild
Any time you make changes to the C++ code, run this command to rebuild and reinstall the wheels...  

`
python -m pip install .
`
