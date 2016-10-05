import subprocess
from hooks_declare import *
from distutils.dir_util import copy_tree


def copy_folder(src, dst):
    # copy subdirectory example
	fromDirectory = src
	toDirectory = dst
	copy_tree(fromDirectory, toDirectory)

# Execute "git diff HEAD~1 HEAD"
def get_diff_between_two_last_commit():
	return execute_git_cmd(["diff", "HEAD~1", "HEAD", "--name-status"], False).strip()

# Execute "git diff --name-status"
def get_diff_name_status() :
	return execute_git_cmd(["diff", "--name-status"], False).strip()

# Execute a command like "git argv..."
def execute_git_cmd(argv, print_it=True):
	full_cmd = argv
	full_cmd.insert(0, git_cmd)
	return execute_cmd(full_cmd, print_it)

"""
will execute the cmd in the system.
the main cmd and each argument have to be in an element of the list
return the value of the command
"""
def execute_cmd(arg_list, print_it=True):
	#create the proc
	proc = subprocess.Popen(arg_list, stdout=subprocess.PIPE)
	#communicate with the proc and get the stdout value
	stdout_value = proc.communicate()[0].decode("utf-8")
	if print_it != False :
		print(stdout_value)
	if proc.returncode != 0 :
		return proc.returncode
	return stdout_value

def get_current_branch_name():
	return execute_git_cmd( [ "rev-parse", "--abbrev-ref", "HEAD"], False ).strip()
