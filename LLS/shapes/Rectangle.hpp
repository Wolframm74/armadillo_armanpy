// A2DD.h
#ifndef A2DD_H
#define A2DD_H

#include <armadillo>

namespace Shapes {

using namespace arma;

class A2DD
{
  //int gx;
  //int gy;

public:
  //A2DD(auto& x_arr, auto& y_arr, int N);
  A2DD(std::array<double, 4ul>& x_arr, std::array<double, 4ul>& y_arr, int N);
  int getParams(double& B1, double& B2);

private:
  mat eq_mat;
  colvec y_vec;
  colvec parameter;

};

}

#endif
