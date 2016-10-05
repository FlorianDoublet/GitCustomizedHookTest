from hooks_util import *
from hooks_files import *
from hooks_declare import *
from shutil import copyfile
from shutil import copy2


def commit_hook(argv):	
	res = execute_git_cmd(argv, False)
	# If the commit success
	if res == 0 :
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
	create_branch_for_commit(sha1)
	
def create_branch_for_commit(sha1):
	execute_git_cmd([ "branch", sha1 ], False)
