cmake_minimum_required(VERSION 3.10)

include(ExternalProject)

get_filename_component(DIR_ONE_ABOVE ../ ABSOLUTE)
message(STATUS ${DIR_ONE_ABOVE})

set(CMAKE_INSTALL_PREFIX ${CMAKE_CURRENT_LIST_DIR}/build/installdir)

#find path for app, to be passed into LLS_lib build
find_path(ARMADILLO_INCLUDE armadillo ${DIR_ONE_ABOVE}/arma_installdir/include)

message(STATUS "${CMAKE_CURRENT_LIST_DIR} ARMADILLO_INCLUDE dir ... ${ARMADILLO_INCLUDE}")

#find library for armadillo.so, to be linked against in LLS_lib
find_library(ARMADILLO_LIBRARY libarmadillo.so PATHS ${DIR_ONE_ABOVE}/arma_installdir/lib)

add_subdirectory(LLS_lib)
add_subdirectory(app)

#use the python script to run make and make install
#execute_process(COMMAND  python install.py WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})

message(STATUS "${CMAKE_CURRENT_LIST_DIR} CMAKE_INSTALL_PREFIX dir ... ${CMAKE_INSTALL_PREFIX}")
