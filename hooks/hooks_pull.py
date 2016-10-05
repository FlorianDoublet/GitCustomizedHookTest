from hooks_util import *
from hooks_refactor import *


def pull_hook(argv):
	#pre_pull 
	pre_pull()
	#command
	execute_git_cmd(argv)
	#post_pull 
	post_pull()
	
def pre_pull():
	nb_commit_to_check = 2
	last_commits = execute_git_cmd(["log",  "--pretty=oneline",  "-n",  str(nb_commit_to_check)], False)
	last_commits = last_commits.splitlines()
	position_in_head = find_position_of_a_commit(last_commits, user_refact_msg)
	
	#On reset le commit
	#On reformat-serv
	#On refait le commit si il y en avait un 
	
	#if the commit was found
	if position_in_head :
		commit_message = None
		if position_in_head != 1 :
			commit_message = last_commits[0].split(" ", 1)[1]
		#reset to HEAD~N	
		git_reset_head(position_in_head)
		
		#we do the server refactor
		srv_refactor(str(commit_message))

def post_pull():
	user_refactor()
	
