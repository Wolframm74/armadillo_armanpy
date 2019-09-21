cmake_minimum_required(VERSION 3.10)

get_filename_component(DIR_ONE_ABOVE ../ ABSOLUTE)
message(STATUS ${DIR_ONE_ABOVE})

find_library(ARMADILLO_LIBRARY libarmadillo.so PATHS ${DIR_ONE_ABOVE}/arma_installdir/lib)

add_subdirectory(shapes)
