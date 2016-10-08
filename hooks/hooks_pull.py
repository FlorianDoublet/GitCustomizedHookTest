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
	commit_list = get_the_x_last_commits(20)
	current_branch = get_current_branch_name()
	unpushed_commit_list = get_unpushed_commit_for_a_branch(current_branch)

	if unpushed_commit_list == None:
		return

	for unpushed_commit in unpushed_commit_list:
		position_in_head = None
		if unpushed_commit == unpushed_commit_list[0] :
			#get the position of the first user refactor commit
			position_in_head_user_refac = find_position_of_a_commit(commit_list ,user_refact_msg)
			position_in_head = find_position_of_a_commit(commit_list ,unpushed_commit["sha1"])

			if position_in_head_user_refac < position_in_head :
				#we reset hard to the head
				git_reset_head_hard(position_in_head)
			else:
				git_reset_head_hard(position_in_head_user_refac)
		else :
			#get the position of the unpushed commit for our branch 
			position_in_head = find_position_of_a_commit(commit_list ,unpushed_commit["sha1"])

		#TODO
		#1 : on va sur la branche du plus vieux commit
		#2 : git reset head en sauvant le message
		#3 : on refactor serveur
		#4 : on re-cree le commit précédent

		#1 :
		commit_branch = unpushed_commit["sha1"]
		change_branch(commit_branch)

		#2
		message = get_the_x_last_commits(1)[0].split(" ", 1)[1]

		if unpushed_commit == unpushed_commit_list[0] :
			#reset head 2 for the will be deleted commit
			git_reset_head(2)
		else :
			git_reset_head(1)

		#3 & 4
		srv_refactor(message)
	change_branch(current_branch)


def post_pull():
	user_refactor()
	
