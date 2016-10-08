from hooks_files import *
from hooks_util import *
import os
import sys
import subprocess
import time

bashrc_path = os.path.expanduser("~/.bashrc")
bashrc_function_path = "hooks/bashrc_function"
files_to_ignore = [ "hooks/.tmp_refac/", "hooks/__pycache__/"]

def main(argv):
	#adding the git function and/or the path of our project into
	add_git_function()
	#create the required conf files
	create_conf_files()
	#ignore unwanted folder or file to be pushed
	gitignore_add_files(files_to_ignore)

	#we ask to the user to run source ~/.bashrc
	print("You now have to run 'source ~/.bashrc' in your shell")

def add_git_function():
	bashrc = read_file(bashrc_path)

	if "function git ()" not in bashrc :
		git_function = read_file(get_root_directory() + bashrc_function_path)
		#we add ou project directory to the bashrc
		git_function = add_directory_in_git_function(get_root_directory()[:-1], git_function)
		#we add the function at the end of our bashrc
		write_file(bashrc_path, git_function)
	else :
		res = add_directory_in_git_function(get_root_directory()[:-1], bashrc)
		if res != None :
			#rewrite file
			write_file(bashrc_path, res, "w")



def add_directory_in_git_function(directory_path, file_str):
	bashrc = file_str.splitlines()
	for (i, line) in enumerate(bashrc):
		if "declare -a indexed_dirs=" in line:
			if directory_path in line:
				return None
			else :
				if "your repo" in line:
					bashrc[i] = line.replace("your repo", directory_path)
				else :
					pos = line.find(")")
					#add our directory into the list
					new_line = line[:pos] + ", \"" + directory_path + "\"" + line[pos:]
					#replace line by new_line
					print("new_line : " + new_line)
					bashrc[i] = new_line
				return bashrc

def create_conf_files():
	get_or_create_tmp_folder()
	create_unpushed_commit_file()

def gitignore_add_files(list_of_files):
	gitignore_path = get_root_directory() + ".gitignore"
	if not os.path.isfile(gitignore_path):
		#we create the file and write of list of files into
		write_file(gitignore_path, list_of_files, "w")
		return
	else:
		gitignore_f = read_file(gitignore_path)
		gitignore_l = []
		for f in list_of_files:
			if f not in gitignore_f:
				gitignore_l.append(f)
		if len(gitignore_l) >= 1 :
			write_file(gitignore_path, gitignore_l)



if __name__ == "__main__":
   main(sys.argv[1:])
