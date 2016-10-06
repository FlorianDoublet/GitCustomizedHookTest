from hooks_util import *
from hooks_refactor import *


def pull_hook(argv):
	#pre_pull 
	pre_pull()
	'''
	#command
	execute_git_cmd(argv)
	#post_pull 
	post_pull()
	'''
	
def pre_pull():
	'''
	nb_commit_to_check = 2
	last_commits = get_the_x_last_commits(nb_commit_to_check)
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
	'''
	commit_list = get_the_x_last_commits(20)
	#current_branch = get_current_branch_name()
	#unpushed_commit_list = get_unpushed_commit_for_a_branch(current_branch)
	unpushed_commit_list = parse_unpushed_commit_tmp()
	if unpushed_commit_list == None:
		return

	for unpushed_commit in unpushed_commit_list:
		'''
		position_in_head = None
		
		if unpushed_commit == unpushed_commit_list[0] :
			#get the position of the first user refactor commit
			position_in_head = find_position_of_a_commit(commit_list ,user_refact_msg)

			#we reset hard to the head
			git_reset_head_hard(position_in_head)
		else :
			#get the position of the unpushed commit for our branch 
			position_in_head = find_position_of_a_commit(commit_list ,unpushed_commit["sha1"])
		'''

		#TODO
		#1 : on va sur la branche du plus vieux commit
		#2 : git reset head en sauvant le message
		#3 : on refactor serveur
		#4 : on re-cree le commit précédent
		#5 : on reviens sur notre branche précédente puis on merge avec la branche du commit
		#6 : on supprime la branch et l'index dans le fichier

		#1 :
		commit_branch = unpushed_commit["sha1"]
		change_branch(commit_branch)

		#2
		message = get_the_x_last_commits(1)[0].split(" ", 1)[1]

		'''
		if unpushed_commit == unpushed_commit_list[0] :
			#reset head 2 for the will be deleted commit
			git_reset_head(2)
		else :
			git_reset_head(1)
		'''
		git_reset_head(1)

		#3 & 4
		srv_refactor(message)
		'''
		#get new commit sha1
		new_sha1 = get_the_x_last_commits(1)[0].split(" ", 1)[0]

		#5
		change_branch(current_branch)

		if unpushed_commit == unpushed_commit_list[0] :
			#on merge simplement les 2 branches
			res = merge_branch(commit_branch)
		else :
			res = cherry_pick_commit(new_sha1)
		
		print(" ---> res : " + str(res))

		#TODO finir la tache 6 !
		#we remove the branch
		execute_git_cmd([ "branch", "-D", commit_branch])
		#and we remove the first line of 
		delete_first_line_unpushed_commit_file_for_branch(current_branch)
		'''

def post_pull():
	user_refactor()
	
