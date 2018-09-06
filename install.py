from subprocess import Popen, PIPE
import os

def append_to_file_newline(file, armadillo_armanpy_installdir):

	appended_text="CXX_INCLUDES += -I"+armadillo_armanpy_installdir

	with open(file, "ab") as myfile:
		myfile.write(appended_text)

def append_flags_make(armadillo_armanpy_installdir):

	file='example/CMakeFiles/_armanpyexample.dir/flags.make'
	append_to_file_newline(file, armadillo_armanpy_installdir+"/include")

	file='example/CMakeFiles/examplelib.dir/flags.make'
	append_to_file_newline(file, armadillo_armanpy_installdir+"/include")

	file='test/CMakeFiles/armanpy_test_lib.dir/flags.make'
	append_to_file_newline(file, armadillo_armanpy_installdir+"/include")

	file='test/CMakeFiles/_armanpytest.dir/flags.make'
	append_to_file_newline(file, armadillo_armanpy_installdir+"/include")

def file_replace_string_link(input_file, input_str, b_rpath):

	str_rpath=""

	if (b_rpath):
		str_rpath=" -Wl,-rpath,"+input_str

	s = open(input_file).read()
	s = s.replace("-larmadillo", "-larmadillo "+"-L"+input_str+str_rpath)
	f = open(input_file, 'w')
	f.write(s)
	f.close()

def append_link_txt(armadillo_armanpy_installdir):

	#Set True to provide arma_installdir/lib as a runtime library search path
	file='example/CMakeFiles/_armanpyexample.dir/link.txt'
	file_replace_string_link(file, armadillo_armanpy_installdir+"/lib", True)

	file='example/CMakeFiles/examplelib.dir/link.txt'
	file_replace_string_link(file, armadillo_armanpy_installdir+"/lib", False)

	file='test/CMakeFiles/armanpy_test_lib.dir/link.txt'
	file_replace_string_link(file, armadillo_armanpy_installdir+"/lib", False)

	#Set True to provide arma_installdir/lib as a runtime library search path
	file='test/CMakeFiles/_armanpytest.dir/link.txt'
	file_replace_string_link(file, armadillo_armanpy_installdir+"/lib", True)

def file_replace_all(retval, LinuxPrefix):

	file='example/CMakeFiles/_armanpyexample.dir/build.make'
	string='bin/_armanpyexample.so: /lib/'+LinuxPrefix+'libarmadillo.so'
	file_replace_string(os.getcwd()+'/'+file, string)

	file='example/CMakeFiles/examplelib.dir/build.make'
	string='bin/libexamplelib.so: /lib/'+LinuxPrefix+'libarmadillo.so'
	file_replace_string(os.getcwd()+'/'+file, string)

	file='test/CMakeFiles/armanpy_test_lib.dir/build.make'
	string='bin/libarmanpy_test_lib.so: /lib/'+LinuxPrefix+'libarmadillo.so'
	file_replace_string(os.getcwd()+'/'+file, string)
	
	file='test/CMakeFiles/_armanpytest.dir/build.make'
	string='bin/_armanpytest.so: /lib/'+LinuxPrefix+'libarmadillo.so'
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

def install_armanpy(retval, bLinuxPrefix):

	if bLinuxPrefix:
		LinuxPrefix='x86_64-linux-gnu/'
	else:
		LinuxPrefix=''

	armadillo_armanpy_dir = os.getcwd()
	os.chdir(armadillo_armanpy_dir+'/armanpy-0.1.4')

	cmd = 'mkdir build'
	run_cmd_via_os(cmd)

	os.chdir('build')

	cmd = 'cmake .. -DCMAKE_BUILD_TYPE=Release -DARMADILLO_INCLUDE_DIR=$ARMA_INSTALLDIR/include -DARMADILLO_LIBRARIES=$ARMA_INSTALLDIR/lib/'+LinuxPrefix+'libarmadillo.so'
	run_cmd_via_os(cmd)	

	#Extra stuff
	retval=0
	file_replace_all(retval, LinuxPrefix)

	#if armadillo is not installed to /usr/include, we need to do some additional modifications
	if not os.path.isfile('/usr/include/armadillo'):
		armadillo_armanpy_installdir=armadillo_armanpy_dir+'/arma_installdir'
		append_flags_make(armadillo_armanpy_installdir)
		append_link_txt(armadillo_armanpy_installdir)

	cmd = 'cmake --build . --config Release'
	run_cmd_via_os(cmd)	

	retval=1

if __name__=="__main__":
	
	retval=0

	#You may need to compile with a specific "LinuxPrefix" depending on your system environment...
	#You can figure this out by compiling armadillo only and checking the output of "arma_installdir/lib"
	bLinuxPrefix=True

	install_armadillo(retval)	
	install_armanpy(retval, bLinuxPrefix)
