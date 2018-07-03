=======
# armadillo_armanpy
Simple build and install of armadillo-8.500.1 and swig based python library armanpy-0.1.4

1. Clone armadillo_armanpy in to some location.
2. Install liblapack, libblas dependencies. 
3. Install Everything. 

Method 1: Manually enter the steps in compile_armadillo.txt, followed by the steps in compile_armanpy.txt

Method 2:
Simply run install.py

	python install.py

4. It is assumed that python has been installed on your system, if Step 3 failed, Step 3a is to install python.
5. Test armanpy by running 
	cd armanpy-0.1.4/build/bin
	python example.py
	python armanpy_test_run.py

Thanks. Please report any bugs to Wolframm74@Github.
