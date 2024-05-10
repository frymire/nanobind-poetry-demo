#include <nanobind/nanobind.h>

NB_MODULE(_hello_impl, m) {
    m.def("hello", []() { return "Whassup, sucka?"; });
}
