#include "Linear_LS.hpp"

namespace LLS {

using namespace arma;

// Take a set of points {x,y}
// Return the least squares solution which is the set of parameters B1, B2
// B1 + x1*B2 = y1
// B1 + x2*B2 = y2
// ...
// B1 + xN*B2 = yN
//

//LLS_impl::LLS_impl(auto& x_arr, auto& y_arr, int N) //assume x_arr and y_arr are doubles
LLS_impl::LLS_impl(std::array<double, 4ul>& x_arr, std::array<double, 4ul>& y_arr, int N): eq_mat(N, 2), y_vec(N), parameter(2) 
{
	eq_mat.ones();

	// Populate the matrix of data and y_vec
	for(int ind = 0; ind < N; ind++ ) 
	{
		eq_mat(ind, 1) = x_arr.at(ind);
		y_vec(ind) = y_arr.at(ind);
	}

	std::cout << "A:\n" << eq_mat << "\n";

}

// Return B1 and B2
int LLS_impl::getParams(double& B1, double& B2)
{
  	//Invert the matrix, as part of the solution
	//From the vector of 2, return B1 and B2
	parameter = pinv(eq_mat)*y_vec;

	B1 = parameter(0);
	B2 = parameter(1);
	
}

}
