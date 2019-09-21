cmake_minimum_required(VERSION 2.8)
project(libtest_project)
add_library(shapes_test Rectangle.cpp)

set(INCLUDE_DIRS ${ARMADILLO_INCLUDE})

message(STATUS "${CMAKE_CURRENT_LIST_DIR} Compiling Shapes library ${INCLUDE_DIRS} ")

include_directories(${INCLUDE_DIRS})

target_include_directories(shapes_test PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

target_include_directories(shapes_test PUBLIC ${INCLUDE_DIRS})

#link armadillo against target
target_link_libraries(shapes_test PRIVATE ${ARMADILLO_LIBRARY})

install(TARGETS shapes_test DESTINATION lib)
install(FILES Rectangle.hpp DESTINATION include)
