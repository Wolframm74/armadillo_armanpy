from subprocess import Popen, PIPE
import os

def file_replace_all(retval):

	file='example/CMakeFiles/_armanpyexample.dir/build.make'
	string='bin/_armanpyexample.so: /lib/x86_64-linux-gnu/libarmadillo.so'
	file_replace_string(os.getcwd()+'/'+file, string)

	file='example/CMakeFiles/examplelib.dir/build.make'
	string='bin/libexamplelib.so: /lib/x86_64-linux-gnu/libarmadillo.so'
	file_replace_string(os.getcwd()+'/'+file, string)

	file='test/CMakeFiles/armanpy_test_lib.dir/build.make'
	string='bin/libarmanpy_test_lib.so: /lib/x86_64-linux-gnu/libarmadillo.so'
	file_replace_string(os.getcwd()+'/'+file, string)
	
	file='test/CMakeFiles/_armanpytest.dir/build.make'
	string='bin/_armanpytest.so: /lib/x86_64-linux-gnu/libarmadillo.so'
	file_replace_string(os.getcwd()+'/'+file, string)

	retval = 1 

def file_replace_string(input_file, input_str):

	s = open(input_file).read()
	s = s.replace(input_str, '#'+input_str)	
	f = open(input_file, 'w')
	f.write(s)
	f.close()

def export_installdir_variable(armadillo_armanpy_installdir):
	cmd='export ARMA_INSTALLDIR='+armadillo_armanpy_installdir+' && echo $ARMA_INSTALLDIR'
	run_cmd_via_os(cmd)

def run_cmd_via_os(cmd):
	p = os.popen(cmd,"r")
	while 1:
	    line = p.readline()
	    if not line: break
	    print line

def run_cmd_via_subprocess(cmd):
	p = Popen(cmd, stdout=PIPE, stderr=PIPE, stdin=PIPE)
	output = p.stdout.read()
	print(output)
	#p.stdin.write(input)


def install_armadillo(retval):

	# Compile armadillo
	armadillo_armanpy_dir = os.getcwd()

	armadillo_armanpy_installdir=armadillo_armanpy_dir+'/arma_installdir'
	export_installdir_variable(armadillo_armanpy_installdir)

	cmd = 'mkdir '+armadillo_armanpy_installdir
	run_cmd_via_os(cmd)

	os.chdir(armadillo_armanpy_dir+'/armadillo-8.500.1')

	cmd = 'cmake . -DCMAKE_INSTALL_PREFIX:PATH='+armadillo_armanpy_dir+'/arma_installdir'
	run_cmd_via_os(cmd)

	cmd = 'make install'
	run_cmd_via_os(cmd)

	os.chdir('..')

	retval=1

def install_armanpy(retval):

	armadillo_armanpy_dir = os.getcwd()
	os.chdir(armadillo_armanpy_dir+'/armanpy-0.1.4')

	cmd = 'mkdir build'
	run_cmd_via_os(cmd)

	os.chdir('build')

	cmd = 'cmake .. -DCMAKE_BUILD_TYPE=Release -DARMADILLO_INCLUDE_DIR=$ARMA_INSTALLDIR/include -DARMADILLO_LIBRARIES=$ARMA_INSTALLDIR/lib/x86_64-linux-gnu/libarmadillo.so'
	run_cmd_via_os(cmd)	

	retval=0
	file_replace_all(retval)	

	cmd = 'cmake --build . --config Release'
	run_cmd_via_os(cmd)	

	retval=1

if __name__=="__main__":
	
	retval=0

	install_armadillo(retval)	
	install_armanpy(retval)
