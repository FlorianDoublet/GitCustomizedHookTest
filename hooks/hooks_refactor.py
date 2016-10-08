from hooks_util import *
from hooks_files import *
from hooks_declare import *

srv_profile = "/home/mickmouette/Documents/OPL/GitCustomizedHookTest/profiles/1/profile1.xml"
client_profile = "/home/mickmouette/Documents/OPL/GitCustomizedHookTest/profiles/2/profile2.xml"
refractor = "/home/mickmouette/Documents/OPL/GitCustomizedHookTest/refactor.jar"
folder = "/home/mickmouette/Documents/OPL/GitCustomizedHookTest/test"

def srv_refactor(commit_msg=None):
	os.system("java -jar " + refractor + " " + srv_profile + " " + folder)
	
	#the rebased commit (if we have to)
	if commit_msg :
		git_add_all()
		git_simple_commit(commit_msg)

	
	
def user_refactor():
	os.system("java -jar " + refractor + " " + client_profile + " " + folder)
	
	#adding all refactored files
	git_add_all()
	
	#then we commit it with our default message
	git_simple_commit(user_refact_msg)