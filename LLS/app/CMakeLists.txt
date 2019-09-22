cmake_minimum_required(VERSION 2.8)

project(app_project)

add_executable(myapp main_app.cpp)

get_filename_component(DIR_ONE_ABOVE ../ ABSOLUTE)

include_directories(${DIR_ONE_ABOVE}/LLS_lib)

target_include_directories(myapp PUBLIC ${CMAKE_INSTALL_PREFIX}/usr/local/include)

#target_include_directories(myapp PRIVATE ${CMAKE_INSTALL_PREFIX}/include)
target_link_libraries(myapp PRIVATE lls_lib)

install(TARGETS myapp DESTINATION bin)
