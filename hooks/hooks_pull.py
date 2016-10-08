from hooks_util import *
from hooks_refactor import *


def pull_hook(argv):
	#pre_pull 
	pre_pull()
	#command
	execute_git_cmd(argv)
	'''
	#post_pull 
	post_pull()
	'''
	
def pre_pull():
	commit_list = get_the_x_last_commits(20)
	current_branch = get_current_branch_name()
	unpushed_commit_list = parse_unpushed_commit_tmp()
	if unpushed_commit_list == None:
		return

	for unpushed_commit in unpushed_commit_list:
		commit_branch = unpushed_commit["sha1"]
		change_branch(commit_branch)
		message = get_the_x_last_commits(1)[0].split(" ", 1)[1]
		git_reset_head(1)
		srv_refactor(message)
	change_branch(current_branch)

def post_pull():
	user_refactor()
	
