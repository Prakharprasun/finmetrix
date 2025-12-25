cmake_minimum_required(VERSION 3.15)
project(finmetrix_cpp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET "11.1" CACHE STRING "" FORCE)
    execute_process(
        COMMAND xcrun --sdk macosx --show-sdk-path
        OUTPUT_VARIABLE CMAKE_OSX_SYSROOT
        OUTPUT_STRIP_TRAILING_WHITESPACE
    )
    set(CMAKE_OSX_SYSROOT "${CMAKE_OSX_SYSROOT}" CACHE PATH "" FORCE)
endif()

find_package(pybind11 REQUIRED)

pybind11_add_module(_cpp
    finmetrix/_backend/cpp/bindings.cpp
    finmetrix/_backend/cpp/twr.cpp
)

install(TARGETS _cpp DESTINATION finmetrix/_backend)
