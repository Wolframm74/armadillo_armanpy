cmake_minimum_required(VERSION 2.8)

project(app_project)

add_executable(myapp main_app.cpp)

install(TARGETS myapp DESTINATION bin)
