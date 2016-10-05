#!/usr/bin/python

import sys
import os
import subprocess
from subprocess import Popen, PIPE
import time
import pexpect
import shutil, errno
from distutils.dir_util import copy_tree



#pathname include the complete path from the source repo
def copy_unpushed_commit_file(sha1, pathname, path_file_to_copy):
	
	#we read the file
	file_str = read_file(path_file_to_copy)
	#creation of the filename
	new_file_name = sha1 + "/" + pathname
	complete_copyfile_path = get_root_directory() + unpushed_commit_folder + new_file_name
	#write the file to the wanted path
	write_file(complete_copyfile_path, file_str, mode="w")

	

def copyanything(src, dst):
    # copy subdirectory example
	fromDirectory = src
	toDirectory = dst

	copy_tree(fromDirectory, toDirectory)


	return root_dir + "/"

if __name__ == "__main__":
   main(sys.argv[1:])
