# noinspection PyProtectedMember
from hello_ext._hello_impl import hello
from numpy import pi


def say_hi() -> None:
    print("Numpy (poetry dependency) says pi =", pi)
    print("C++ extension (via nanobind) says hi...", hello())


def main():
    say_hi()


if __name__ == '__main__':
    main()
