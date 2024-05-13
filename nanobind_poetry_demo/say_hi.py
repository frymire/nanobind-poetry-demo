from hello_ext.hello_impl import say_hi_cpp, say_bye_cpp
from numpy import pi


def say_hi() -> None:
    print("numpy (poetry dependency) says pi =", pi)
    print("hello_ext (c++ via nanobind) says hi...", say_hi_cpp())


def say_bye() -> None:
    print("hello_ext (c++ via nanobind) says hi...", say_bye_cpp())


def main():
    say_hi()
    say_bye()


if __name__ == '__main__':
    main()
