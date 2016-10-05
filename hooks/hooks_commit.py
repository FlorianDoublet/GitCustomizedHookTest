from hooks_util import *
from hooks_files import *
from hooks_declare import *

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
	tmp_folder_commit = get_or_create_tmp_commit_folder(sha1)

	write_file(tmp_folder + "/" + unpushed_commit_file_name, sha1 + " " + branch_name + " " + message)
	write_file(tmp_folder_commit + "/" + unpushed_commit_file_status, status)
