cmake_minimum_required(VERSION 2.8)
project(libtest_project)
add_library(lls_lib SHARED Linear_LS.cpp array_utility.cpp ext_intf.cpp)

set(INCLUDE_DIRS ${ARMADILLO_INCLUDE})

message(STATUS "${CMAKE_CURRENT_LIST_DIR} Compiling Shapes library ${INCLUDE_DIRS} ")

include_directories(${INCLUDE_DIRS})

target_include_directories(lls_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

target_include_directories(lls_lib PUBLIC ${INCLUDE_DIRS})

#link armadillo against target
target_link_libraries(lls_lib PRIVATE ${ARMADILLO_LIBRARY})

install(TARGETS lls_lib DESTINATION lib)
install(FILES Linear_LS.hpp array_utility.hpp ext_intf.hpp DESTINATION include)
