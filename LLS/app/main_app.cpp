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

	std::array<double, 4> arr_x = {1, 2, 3, 4};
	std::array<double, 4> arr_y = {6, 5, 7, 10};

	std::cout << "add rows 1 and 3, store rsadfffffffffffffffffffffffi:\n";

	//std::cout << "x vector:\n" << arr_x << "\n";
	//std::cout << "y vector:\n" << arr_y << "\n";

	// compute it 
	Shapes::A2DD c=Shapes::A2DD(arr_x, arr_y, 4);
	
	double B1, B2;
	
	// check that this seems right ...
	c.getParams(B1, B2);

	//std::cout << "B1:\n" << B1 << "\n";
	//std::cout << "B2:\n" << B2 << "\n";

}

