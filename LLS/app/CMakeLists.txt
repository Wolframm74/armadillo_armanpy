cmake_minimum_required(VERSION 2.8)

project(app_project)

add_executable(myapp main_app.cpp)

target_include_directories(myapp PRIVATE ${CMAKE_INSTALL_PREFIX}/usr/local/include)
target_link_libraries(myapp PRIVATE shapes_test)

install(TARGETS myapp DESTINATION bin)
