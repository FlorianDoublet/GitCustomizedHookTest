from hooks_util import *
from hooks_files import *
from hooks_declare import *
from shutil import copyfile
from shutil import copy2


def commit_hook(argv):	
	res = execute_git_cmd(argv, False)
	# If the commit success
	if type(res) is str :
		post_commit()
	
def post_commit():
	status = ""
	sha1 = ""
	branch_name = ""
	message = ""
	
	status = get_diff_between_two_last_commit()
	branch_name = get_current_branch_name()
	log_res = execute_cmd( [ git_cmd, "log",  "--pretty=format:%h %B",  "-n",  "1" ], False )
	log_values = log_res.split(" ", 1)
	sha1 = log_values[0]

	message = log_values[1]
	tmp_folder = get_or_create_tmp_folder()

	write_file(tmp_folder + unpushed_commit_file_name, sha1 + " " + branch_name + " " + message)
	create_branch_for_commit(sha1)
	
def create_branch_for_commit(sha1):
	execute_git_cmd([ "branch", sha1 ], False)


def recreate_unpushed_commits():
	#TODO : finir ca
	
	#unpushed_commit_info_list = parse_unpushed_commit_tmp()
	
	
	#test copy folder
	copyanything(get_root_directory() + unpushed_commit_folder + "shadir", get_root_directory())
	
	
	#for commit_hash in unpushed_commit_info_list:
	unpushed_commit_list = parse_unpushed_commit_tmp()
	
	for commit_hash in unpushed_commit_list:
		unpushed_commit = get_root_directory() + unpushed_commit_folder + commit_hash["sha1"]
		#copy all the file 
		copyanything(unpushed_commit, get_root_directory())
		#gerer les cas chiant PLUS TARD



