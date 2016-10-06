from hooks_util import *
from hooks_files import *
from hooks_declare import *
from hooks_commit import *
from hooks_refactor import *


def push_hook(argv):
	print("push hook")
	
	#first, pre_push operations
	pre_push()

	#and we process to the server_refactoring
	"""
	srv_refactor(commit_msg)

	res = execute_git_cmd(argv)
	
	
	if res != 0 :
		print("on verra")
	#then post_push operations
	post_push()
	"""

def pre_push():

	"""
	#get the two last commit sha1 and message
	two_last_commit = execute_git_cmd( [ "log",  "--pretty=oneline",  "-n",  "2" ], print_it=False)
	#get the messages of the commits
	first_commit_sha1_msg = two_last_commit.splitlines()[0].split(" ", 1)
	second_commit_sha1_msg = two_last_commit.splitlines()[1].split(" ", 1)
	
	#default param if the last commit is the user refactor commit
	commit_msg = None
	head = 1
	
	#if the first commit isn't the refactor user commit
	if user_refact_msg != first_commit_sha1_msg[1] :
		head += 1
		commit_msg = first_commit_sha1_msg[1]
	
	#then we reset the commit(s)
	git_reset_head(head)
	return commit_msg"""


	commit_list = get_the_x_last_commits(20)
	current_branch = get_current_branch_name()
	unpushed_commit_list = get_unpushed_commit_for_a_branch(current_branch)
	if unpushed_commit_list == None:
		return

	oldest_commit = unpushed_commit_list[0]

	#get the position of the first unpushed commit for our branch
	position_in_head = find_position_of_a_commit(commit_list ,user_refact_msg)


	#we reset hard to the head
	git_reset_head_hard(position_in_head)

	#TODO
	#1 : on va sur la branche du plus vieux commit
	#2 : git reset head en sauvant le message
	#3 : on refactor serveur
	#4 : on re-cree le commit précédent
	#5 : on reviens sur notre branche précédente puis on merge avec la branche du commit
	#6 : on supprime la branch et l'index dans le fichier

	#1 :
	commit_branch = oldest_commit["sha1"]
	change_branch(commit_branch)

	#2
	message = get_the_x_last_commits(1)[0].split(" ", 1)[1]

	#reset head 2 for the will be deleted commit
	git_reset_head(2)

	#3 & 4
	srv_refactor(message)

	#5
	change_branch(current_branch)
	res = merge_branch(commit_branch)

	#TODO finir la tache 6 !
	#we remove the branch
	execute_git_cmd([ "branch", "-d", commit_branch])
	#and we remove the first line of 
	delete_first_line_unpushed_commit_file_for_branch(current_branch)




def post_push():
	#we simply apply the user_refactor process
	user_refactor()
