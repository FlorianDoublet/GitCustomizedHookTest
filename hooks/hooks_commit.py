from hooks_util import *
from hooks_files import *
from hooks_declare import *
from shutil import copyfile
from shutil import copy2

def commit_hook(argv):	
	#execute_git_cmd(argv, False)
	post_commit()
	
def post_commit():
	status = ""
	sha1 = ""
	branch_name = ""
	message = ""
	
	status = get_diff_between_two_last_commit()
	branch_name = execute_cmd( [ git_cmd, "rev-parse", "--abbrev-ref", "HEAD"], print_it=False ).strip()
	log_res = execute_cmd( [ git_cmd, "log",  "--pretty=oneline",  "-n",  "1" ], print_it=False )
	log_values = log_res.split(" ", 1)
	sha1 = log_values[0]
	message = log_values[1]
	
	tmp_folder = get_or_create_tmp_folder()

	write_file(tmp_folder + "/" + unpushed_commit_file_name, sha1 + " " + branch_name + " " + message)



def add_tmp_commit_files(status, tmp_folder_commit):
	file_str_array = status.splitlines()
	
	for line in file_str_array:
		l_parse = line.split("\t", 1)
		if l_parse[0] == "M" or l_parse[0] == "A" :
			src = get_root_directory() + "/" + l_parse[1]
			print(src)
			copyfile(src, tmp_folder_commit)


def create_branch_for_commit(sha1):
	execute_git_cmd([ "branch", sha1 ], False)


	
