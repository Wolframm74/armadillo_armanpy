#include "ext_intf.hpp"
#include "Linear_LS.hpp"

extern "C" void foo(int count, double** array, int size){

   int ii,jj;
   for (ii=0;ii<count;ii++){
      for (jj=0;jj<size;jj++)
         array[ii][jj] *= 2;    
   }

}

/*
** \brief LLS solver for vectors x,y of size N and parameter Beta of size M, e.g N=4, M=2
*/
extern "C" void lls_solver(double* x_array, double* y_array, int vector_size, double* beta_solution, int b_size){

std::vector<double> x_arr(x_array, x_array+vector_size);
std::vector<double> y_arr(y_array, y_array+vector_size);
std::vector<double> B_param(beta_solution, beta_solution+b_size);

//B_param.reserve(b_size);

/* Create the solver */
LLS::LLS_impl ls_sol(x_arr, y_arr, vector_size, B_param, b_size);

/* Make it compute the solution */
ls_sol.solveLLS();

for (int i = 0; i < b_size; i++){
	// Return the solution to the outside world
	*(beta_solution+i)=B_param.at(i);	
}

}
