from hello_ext.hello_impl import say_hi_cpp
from numpy import pi


def say_hi() -> None:
    print("numpy (poetry dependency) says pi =", pi)
    print("hello_ext (c++ via nanobind) says hi...", say_hi_cpp())


def main():
    say_hi()


if __name__ == '__main__':
    main()
