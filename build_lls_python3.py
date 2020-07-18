from subprocess import Popen, PIPE
import os

def run_cmd_via_os(cmd):
        p = os.popen(cmd,"r")
        while 1:
            line = p.readline()
            if not line: break
            print(line)

if __name__=="__main__":

	os.chdir('LLS/build')

	run_cmd_via_os("./buildall.sh")
