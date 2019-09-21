cmake_minimum_required(VERSION 2.8)
project(libtest_project)
add_library(shapes_test STATIC Rectangle.cpp)

#link armadillo against target
target_link_libraries(shapes_test PRIVATE ${ARMADILLO_LIBRARY})

install(TARGETS shapes_test DESTINATION lib)
install(FILES Rectangle.hpp DESTINATION include)
