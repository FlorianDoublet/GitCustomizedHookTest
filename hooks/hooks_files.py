import os
from hooks_util import *
from hooks_declare import *


# Files

def write_file(path, data, mode="a+"):
	f = open(path, mode)
	f.write(data)
	f.close()

# Folders

def get_or_create_tmp_commit_folder(sha1):
	path = get_or_create_tmp_folder() + "/" + sha1
	
	if not os.path.exists(path):
		os.makedirs(path)
	
	return path

def get_or_create_tmp_folder() :
	path = get_root_directory() + "/" + unpushed_commit_folder
	
	if not os.path.exists(path):
		os.makedirs(path)
	
	return path

def get_root_directory():
	return execute_cmd([ git_cmd, "rev-parse" ,"--show-toplevel"], print_it=False).strip()


def read_file(path):
	f = open(path, 'r')
	file_str = f.read()
	f.close()
	return file_str

def delete_folder_with_files(path):
	shutil.rmtree(path)