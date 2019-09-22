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
	file_replace_string(os.getcwd()+'/'+file, string, '#'+string)

	file='example/CMakeFiles/examplelib.dir/build.make'
	string='bin/libexamplelib.so: /lib/'+LinuxPrefix+'libarmadillo.so'
	file_replace_string(os.getcwd()+'/'+file, string, '#'+string)

	file='test/CMakeFiles/armanpy_test_lib.dir/build.make'
	string='bin/libarmanpy_test_lib.so: /lib/'+LinuxPrefix+'libarmadillo.so'
	file_replace_string(os.getcwd()+'/'+file, string, '#'+string)

	file='test/CMakeFiles/_armanpytest.dir/build.make'
	string='bin/_armanpytest.so: /lib/'+LinuxPrefix+'libarmadillo.so'
	file_replace_string(os.getcwd()+'/'+file, string, '#'+string)

	retval = 1

def check_CXX_INCLUDES_missing(file):

	filebuf=open(file)
	text=filebuf.read().strip().split()

	if not "CXX_INCLUDES" in text:
		print("CXX_INCLUDES missing! from "+str(file))
		return True

#I've observed that cmake can forget to add the variable CXX_INCLUDES to the build.make files, this function checks for it and adds it in.
def file_replace_all_(retval, LinuxPrefix):

	string='$(CXX_DEFINES) $(CXX_FLAGS)'
	replace_with='$(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS)'

	file='example/CMakeFiles/_armanpyexample.dir/build.make'
	if check_CXX_INCLUDES_missing(file):
		file_replace_string(os.getcwd()+'/'+file, string, replace_with)

	file='example/CMakeFiles/examplelib.dir/build.make'
	if check_CXX_INCLUDES_missing(file):
		file_replace_string(os.getcwd()+'/'+file, string, replace_with)

	file='test/CMakeFiles/armanpy_test_lib.dir/build.make'
	if check_CXX_INCLUDES_missing(file):
		file_replace_string(os.getcwd()+'/'+file, string, replace_with)

	file='test/CMakeFiles/_armanpytest.dir/build.make'
	if check_CXX_INCLUDES_missing(file):
		file_replace_string(os.getcwd()+'/'+file, string, replace_with)

	retval = 1

def file_replace_string(input_file, input_str, input_str_replace_with):

	s = open(input_file).read()
	s = s.replace(input_str, input_str_replace_with)
	f = open(input_file, 'w')
	f.write(s)
	f.close()

def export_installdir_variable(armadillo_armanpy_installdir):
	cmd='export ARMA_INSTALLDIR='+armadillo_armanpy_installdir+' && echo $ARMA_INSTALLDIR'
	run_cmd_via_os(cmd)

	if not "ARMA_INSTALLDIR" in os.environ:
		os.environ['ARMA_INSTALLDIR']=armadillo_armanpy_installdir
		print(os.environ['ARMA_INSTALLDIR'])

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

#return true if the library exists at the given prefix location
#if it's not there, assume it's in the prefix location so return false.
def check_prefix(input_str):
	print(input_str)
	return os.path.exists(input_str+'libarmadillo.so')

#return true iff 
def install_armadillo(retval):

	# Compile armadillo
	armadillo_armanpy_dir = os.getcwd()

	armadillo_armanpy_installdir=armadillo_armanpy_dir+'/arma_installdir'
	export_installdir_variable(armadillo_armanpy_installdir)

	cmd = 'mkdir '+armadillo_armanpy_installdir
	run_cmd_via_os(cmd)

	os.chdir(armadillo_armanpy_dir+'/armadillo-8.500.1')

	cmd = 'mkdir build'
        run_cmd_via_os(cmd)

	os.chdir('build')

	cmd = 'cmake .. -DCMAKE_INSTALL_PREFIX:PATH='+armadillo_armanpy_dir+'/arma_installdir'


	print("install_armadillo install_armadillo install_armadillo, cmd {}".format(cmd))

	cmd = 'cmake ..'
	run_cmd_via_os(cmd)

	cmd = 'make install'
	run_cmd_via_os(cmd)

	os.chdir('../../')

	# Determine where the library was installed
	if (check_prefix(armadillo_armanpy_dir+'/arma_installdir/lib/')):
		return False	#If you get back True, no Linux Prefix is needed...
	else:
		return True	#If you get back False, set bLinuxPrefix True!!

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
	file_replace_all_(retval, LinuxPrefix)

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
	####bLinuxPrefix=True

	bLinuxPrefix=install_armadillo(retval)	
	install_armanpy(retval, bLinuxPrefix)
