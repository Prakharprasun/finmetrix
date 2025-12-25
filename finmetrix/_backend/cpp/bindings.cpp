// finmetrix/_backend/cpp/bindings.cpp
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "twr.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_cpp, m) {
    m.doc() = "finmetrix C++ backend (optional acceleration)";
    m.def("twr", &finmetrix::twr, py::arg("returns"));
}
