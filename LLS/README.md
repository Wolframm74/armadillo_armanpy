Implement a linear least square interpolator, as in https://en.wikipedia.org/wiki/Linear_least_squares#Example

using `Armadillo` http://arma.sourceforge.net/docs.html

# How to build & run the example

1. From armadillo_armanpy source directory, run
`cmake .` 
Build output of armadillo armadillo-8.500.1 should be in `armadillo_armanpy/armadillo-8.500.1/build` and `armadillo_armanpy/arma_installdir`.

2. More build stuff should be in `armadllo_armanpy/LLS/build` which is the build directory where the example app will reside.
If armadillo_armanpy/arma_installdir/lib/libarmadillo.so has been successfully built from step 1, then you can rebuild the example app code with the following script
in `armadllo_armanpy/LLS/build`</br>
```./buildall.sh```

3. Output from example app, 

```
user@userpc:~/armadillo_armanpy/LLS/build$ ./app/myapp

Let's do a linear least squares interpolation of vectors x and y

x = [1, 2, 3, 4]

y = [6, 5, 7, 10]'

A = [B1, 1*B2]

    [B1, 2*B2]

    [B1, 3*B2]

    [B1, 4*B2]

Where A = x * [B1, B2] 

and we'd like to solve for the vector of params, p=[B1, B2], that we seek but is unknown!!!!

-- but, not to worry -- we'll have some help from Armadillo, with that.

Substituting the values of x into A, we obtain

A:
   1.0000   1.0000
   1.0000   2.0000
   1.0000   3.0000
   1.0000   4.0000

by doing p = A^[+] * y, where A^[+] is the pseudoinverse of A. (**)

Solution::::

B1: 3.5
B2: 1.4

Note that, p=[3.5, 1.4] parametrizes the line y[i]=B2*x[i]+B1 for i=1:N=4, 

which according to the LLS solution is actually the 'line of best fit'.
```

(**) </br>
https://en.wikipedia.org/wiki/Moore-Penrose_inverse </br> http://arma.sourceforge.net/docs.html#pinv

