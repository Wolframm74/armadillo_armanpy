=======
# armadillo_armanpy
Simple build and install of armadillo-8.500.1 and swig based python library armanpy-0.1.4
Created and tested to work on Debian based Linux.

1. Clone armadillo_armanpy in to some location.
2. Install liblapack, libblas dependencies. Also install cmake. 
3. Install Everything. 

Method 1: Manually enter the steps in compile_armadillo.txt, followed by the steps in compile_armanpy.txt

Method 2:
Simply run install.py

	python install.py

4. It is assumed that python has been installed on your system, if Step 3 failed, Step 3a is to install python. Start with the following dependencies [libpython2.7-dev, libpython3.4-dev, python-dev, python3-dev, libpython-dev, libpython3-dev]. Also ensure that SWIG is installed and the Boost C++ libraries. i.e. 'swig' and 'libboostx.xx-dev'. 
5. The install script first tries to compile armadillo, then armanpy. The armadillo header files and library are installed to the directory specified by CMAKE_INSTALL_PREFIX. This is configured to be so called 'arma_installdir'. 
6. If install.py runs to completion, test armanpy by then running 
	cd armanpy-0.1.4/build/bin,
	python example.py,
	python armanpy_test_run.py
The tests should complete, showing some results, i.e. some matrices being printed out.
7. Since no .gitignore file is provided, clear out junk with 'git clean -xdf'. If you encounter any errors, you may need to return to a previous step and self-resolve. Please share the fix if you find any thing that can be improved.

Thank you for using and contributing to the software. Please report any bugs to 27311681+Wolframm74@users.noreply.github.com
