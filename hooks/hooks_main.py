import sys
from hooks_util import *
from hooks_commit import *

def main(argv):
	if "pull" in argv :
		print("custom pull")
		#pull_hook(argv)
	elif "push" in argv :
		print("custom push")
		#push_hook(argv)
	elif "commit" in argv :
		print("custom commit")
		commit_hook(argv)
	else :
		print("original command")
		execute_git_cmd(argv, True)

if __name__ == "__main__":
   main(sys.argv[1:])
