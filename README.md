# nanobind-wheel-demo
Proof that I can use poetry with nanobind to call C++ from Python

## Build
Open this repo in PyCharm, setting up a local virtual environment with python 3.10.+ as the interpreter. Then, build and install the wheel...  

`
python -m pip install ./hello
`  

If you make changes to the C++ code, re-run this command.

## Run
`
python ./hello/invoke_it.py
`
