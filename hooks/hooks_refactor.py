from hooks_util import *
from hooks_files import *
from hooks_declare import *

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