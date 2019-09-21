#!/bin/sh

cmake ..
make -f Makefile shapes-target
make -f Makefile myapp
