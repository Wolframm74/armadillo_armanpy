project(armadillo_armanpy)

if (PYTHON3)
execute_process(COMMAND python3 install_python3.py WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})
else()
execute_process(COMMAND python install.py WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})
endif()

message(STATUS "STATUS ${CMAKE_CURRENT_LIST_DIR} Done calling install.py")

message(STATUS "STATUS ${CMAKE_CURRENT_LIST_DIR} Starting compilation of linear least squarea example (LLS)")

if (PYTHON3)
execute_process(COMMAND python3 build_lls_python3.py WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})
else()
execute_process(COMMAND python build_lls.py WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})
endif()

#add_subdirectory(LLS)
