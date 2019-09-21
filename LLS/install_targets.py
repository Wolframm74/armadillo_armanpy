from subprocess import Popen, PIPE
import os

if __name__=="__main__":

	# make shapes
	# cd build
	# make shapes

	# make install shapes
	export DESTDIR="$(pwd)/shapes_installdir" && make -j4 install

	# make app
	# cd build
	# make app
