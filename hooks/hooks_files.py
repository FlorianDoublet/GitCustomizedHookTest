import os
from hooks_declare import *
import hooks_util


# Files

def write_file(path, data, mode="a+"):
	f = open(path, mode)
	if type(data) is list:
		f.write("\n".join(data))
	else:
		f.write(data)
	f.close()

def create_unpushed_commit_file():
	unpushed_commit_file_path = get_or_create_tmp_folder() + unpushed_commit_file_name
	if not os.path.isfile(unpushed_commit_file_path):
		open(unpushed_commit_file_path, 'a').close()

# Folders

def get_or_create_tmp_commit_folder(sha1):
	path = get_or_create_tmp_folder() + "/" + sha1
	
	if not os.path.exists(path):
		os.makedirs(path)
	
	return path

def get_or_create_tmp_folder() :
	path = hooks_util.get_root_directory() + unpushed_commit_folder
	
	if not os.path.exists(path):
		os.makedirs(path)
	
	return path



def read_file(path):
	f = open(path, 'r')
	file_str = f.read()
	f.close()
	return file_str

def delete_folder_with_files(path):
	shutil.rmtree(path)

def delete_first_line_unpushed_commit_file_for_branch(branch):
	unpushed_commit_file_path = hooks_util.get_root_directory() + unpushed_commit_folder + unpushed_commit_file_name
	file_str = read_file(unpushed_commit_file_path).splitlines()

	#delete the first occurence found
	for line in file_str:
		if branch in line:
			file_str.remove(line)
			break
	#rewrite the file
	write_file(unpushed_commit_file_path, file_str[1:], "w")
