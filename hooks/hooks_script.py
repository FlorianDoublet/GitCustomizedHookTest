#!/usr/bin/python

import sys
import os
import subprocess
from subprocess import Popen, PIPE
import time
import pexpect

hooked_commands = ["pull", "push"]
git_cmd = "/usr/bin/git"
user_refact_msg = "user refactor (will be deleted)"

def main(argv):

	if "pull" in argv :
		pull_hook(argv)
	elif "push" in argv :
		push_hook(argv)
	else :
		print("commande originale.")
		full_cmd = argv
		full_cmd.insert(0, git_cmd)
		execute_cmd(full_cmd)

	

def pull_hook(argv):
	#pre_pull 
	pre_pull()

	full_cmd = argv
	full_cmd.insert(0, git_cmd)
	#launch the real pull cmb given by the user
	res = execute_cmd(full_cmd)
		
	#post_pull 
	res = post_pull()

def pre_pull():
	nb_commit_to_check = 2
	last_commits = execute_cmd( [ git_cmd, "log",  "--pretty=oneline",  "-n",  str(nb_commit_to_check) ], print_it=False )
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
	

#find the positon of a commit in HEAD thank to his message
def find_position_of_a_commit(commit_list, commit_message):
	head = 1;
	for commit in commit_list :
		if commit_message in commit :
			return head
		else :
			head += 1
	return None
	
def push_hook(argv):
	print("push hook")
	
	#first, pre_push operations
	commit_msg = pre_push()

	#and we process to the server_refactoring
	srv_refactor(commit_msg)
	
	#we push it with the real push cmd given by the user
	full_cmd = argv
	full_cmd.insert(0, git_cmd)
	res = execute_cmd(full_cmd)
	
	
	if res != 0 :
		print("on verra")
	#then post_push operations
	post_push()

def pre_push():
	#get the two last commit sha1 and message
	two_last_commit = execute_cmd( [ git_cmd, "log",  "--pretty=oneline",  "-n",  "2" ], print_it=False)
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
	

def srv_refactor(commit_msg=None):
	
	#TODO : le refactoring server
	#Du coup je fait un mock pour le moment
	os.system("python3 mock_refac_srv.py")
	
	#the rebased commit (if we have to)
	if commit_msg :
		git_add_all()
		git_simple_commit(commit_msg)
	
	
def user_refactor():
	#TODO : le user refactoring
	#Du coup je fait un mock pour le moment
	os.system("python3 mock_refac_usr.py")
	
	
	#adding all refactored files
	git_add_all()
	
	#then we commit it with our default message
	git_simple_commit(user_refact_msg)

	
def git_simple_commit(message):
	return execute_cmd([git_cmd, "commit", "-m", message ], print_it=False)

def git_reset_head(head):
	execute_cmd( [ git_cmd, "reset",  ("HEAD~" + str(head)) ], print_it=False)
	
def git_add_all():
	execute_cmd( [ git_cmd, "add", "--all"  ], print_it=False)
	
	
def array_to_string(argv):
	arg_string = ""
	for arg in argv :
		arg_string += arg + " "
	return arg_string
	
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


if __name__ == "__main__":
   main(sys.argv[1:])
