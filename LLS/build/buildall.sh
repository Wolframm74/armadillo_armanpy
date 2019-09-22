#!/bin/sh

cmake ..

mkdir installdir
make -f Makefile lls_lib
make DESTDIR=$(pwd)/installdir install
make -f Makefile myapp
