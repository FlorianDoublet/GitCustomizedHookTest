from hooks_util import *
from hooks_files import *
from hooks_declare import *
from hooks_commit import *
from hooks_refactor import *

def push_hook(argv):
	print("push hook")
	
	#first, pre_push operations
	commit_msg = pre_push()

	#and we process to the server_refactoring
	srv_refactor(commit_msg)

	res = execute_git_cmd(argv)
	
	
	if res != 0 :
		print("on verra")
	#then post_push operations
	post_push()

def pre_push():
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
	return commit_msg


def post_push():
	#we simply apply the user_refactor process
	user_refactor()