#ifndef A2DD_H
#define A2DD_H

#include <armadillo>
#include "array_utility.hpp"

namespace LLS {

using namespace arma;

class LLS_impl
{

public:
  LLS_impl(std::vector<double>& x_arr, std::vector<double>& y_arr, int N, std::vector<double>& b_param, int M);
  void solveLLS();
  int getParams(double& B1, double& B2);

private:
  mat eq_mat;
  colvec y_vec;
  colvec parameter;
  std::vector<double>& beta_param;
  int N_size;
  int M_size;
};

}

#endif
