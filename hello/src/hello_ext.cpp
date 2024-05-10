#include <nanobind/nanobind.h>

NB_MODULE(hello_impl, m) {
    m.def("say_hi_cpp", []() { return "Whassup, sucka?"; });
    m.def("say_bye_cpp", []() { return "So nice to see you (go)."; });
}
