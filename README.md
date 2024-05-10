# nanobind-wheel-demo
Proof that I can build a nanobind wheel to call C++ functions from Python

## Build
Open this repo in PyCharm, setting up a local virtual environment with python 3.10.+ as the interpreter. Then, build and install the wheel...  

`
python -m pip install .
`  

If you make changes to the C++ code, re-run this command.

## Run
`
python invoke_it.py
`
