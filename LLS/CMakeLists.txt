cmake_minimum_required(VERSION 3.10)

include(ExternalProject)

get_filename_component(DIR_ONE_ABOVE ../ ABSOLUTE)
message(STATUS ${DIR_ONE_ABOVE})

set(CMAKE_INSTALL_PREFIX ${CMAKE_CURRENT_LIST_DIR}/build/installdir)

#find path for app, to be passed into shapes build
find_path(ARMADILLO_INCLUDE armadillo ${DIR_ONE_ABOVE}/arma_installdir/include)

message(STATUS "${CMAKE_CURRENT_LIST_DIR} ARMADILLO_INCLUDE dir ... ${ARMADILLO_INCLUDE}")

#find library for armadillo.so, to be linked against in shapes
find_library(ARMADILLO_LIBRARY libarmadillo.so PATHS ${DIR_ONE_ABOVE}/arma_installdir/lib)

add_subdirectory(shapes)
add_subdirectory(app)

#use the python script to run make and make install
#execute_process(COMMAND  python install.py WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})

#ExternalProject_Add(shapes-target
#	SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/shapes
#        BUILD_COMMAND
#                make -f Makefile shapes_test
#
#	INSTALL_COMMAND
#		make DESTDIR=${CMAKE_INSTALL_PREFIX} install 
#)


#ExternalProject_Add(app-target
#	DEPENDS 
#		shapes-target
#	SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/app
#	BUILD_COMMAND
#		make -f myapp
#)

message(STATUS "${CMAKE_CURRENT_LIST_DIR} CMAKE_INSTALL_PREFIX dir ... ${CMAKE_INSTALL_PREFIX}")
