from hooks_util import *

def commit_hook(argv):	
	#execute_git_cmd(argv, False)
	post_commit()
	
def post_commit():
	status = get_diff_between_two_last_commit()
	print(status)
