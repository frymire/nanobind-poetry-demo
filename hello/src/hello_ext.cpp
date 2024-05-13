#include <nanobind/nanobind.h>

char* say_hi_cpp() {
    return "Whassup, sucka?";
}

char* say_bye_cpp() {
    return "See ya. Wouldn't wanna be ya.";
}

NB_MODULE(hello_impl, m) {
    m.def("say_hi_cpp", &say_hi_cpp);
    m.def("say_bye_cpp", &say_bye_cpp);
}
