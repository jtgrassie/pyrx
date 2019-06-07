cmake_minimum_required(VERSION 2.8.12)
project(pyrx)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(external/pybind11)
add_subdirectory(external/RandomX)
include_directories(${RANDOMX_INCLUDE})
pybind11_add_module(pyrx src/main.cpp src/rx-slow-hash.c)
target_link_libraries(pyrx PRIVATE randomx)

