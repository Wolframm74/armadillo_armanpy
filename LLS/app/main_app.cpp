#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <armadillo>
#include <Linear_LS.hpp>

int main(int argc, char* argv[]){
	
	std::cout << "Let's do a linear least squares interpolation of vectors x and y\n" << "\n";
	std::cout << "x = [1, 2, 3, 4]'\n" << "\n";
	std::cout << "y = [6, 5, 7, 10]'\n" << "\n";

        std::cout << "A = [B1, 1*B2]\n" << "\n";
        std::cout << "    [B1, 2*B2]\n" << "\n";
	std::cout << "    [B1, 3*B2]\n" << "\n";
	std::cout << "    [B1, 4*B2]\n" << "\n";

	std::cout << "Where A = x * [B1, B2] \n" << "\n";

	std::cout << "and we'd like to solve for the vector of params, p=[B1, B2], that we seek but is unknown!!!!\n" << "\n";

	std::cout << "-- but, not to worry -- we'll have some help from Armadillo, with that.\n\n";

	std::vector<double> arr_x = {1, 2, 3, 4};
        std::vector<double> arr_y = {6, 5, 7, 10};
	std::vector<double> param_b = {0, 0};

	std::cout << "Substituting the values of x into A, we obtain\n" << "\n";

        // compute it 
        LLS::LLS_impl lls=LLS::LLS_impl(arr_x, arr_y, 4, param_b, 2);

	lls.solveLLS();

	double B1, B2;

	// check that this seems right ...
	lls.getParams(B1, B2);

	std::cout << "by doing p = A^[+] * y, where A^[+] is the pseudoinverse of A.\n" << "\n";

	std::cout << "Solution::::\n\n";
	std::cout << "B1: " << B1 << "\n";
        std::cout << "B2: " << B2 << "\n\n";

	std::cout << "Note that, p = [3.5, 1.4]' parametrizes the line y[i] = B2*x[i] + B1 for i=1:N=4, \n\nwhich according to the LLS solution is actually the 'line of best fit'.\n";

}

