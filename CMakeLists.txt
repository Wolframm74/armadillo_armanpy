project(armadillo_armanpy)

execute_process(COMMAND  python install.py WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})

message(STATUS "STATUS ${CMAKE_CURRENT_LIST_DIR} Done calling install.py")

message(STATUS "STATUS ${CMAKE_CURRENT_LIST_DIR} Starting compilation of linear least squarea example (LLS)")

add_subdirectory(LLS)
