#!/bin/sh

cmake ..

mkdir installdir
make -f Makefile shapes_test
make DESTDIR=$(pwd)/installdir install
make -f Makefile myapp
