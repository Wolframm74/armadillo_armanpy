#include <stdio.h>
#include <unistd.h>
#include <iostream>
#include <armadillo>
#include <Rectangle.hpp>

int main(int argc, char* argv[]){

	printf("Hello world eh\n");

	// Initialize the random generator
	// Create a 4x4 random matrix and print it on the screen
 	arma::Mat<double> A = arma::randu(4,4);
	std::cout << "A:\n" << A << "\n";

	// Multiply A with his transpose:
	std::cout << "A * A.t() =\n";
	std::cout << A * A.t() << "\n";

	// Access/Modify rows and columns from the array:
	A.row(0) = A.row(1) + A.row(3);
	A.col(3).zeros();
	std::cout << "add rows 1 and 3, store result in row 0, also fill 4th column with zeros:\n";
	std::cout << "A:\n" << A << "\n";



	int x,y;
	x=1;
	y=2;

	A2DD c=A2DD(x,y);


}

