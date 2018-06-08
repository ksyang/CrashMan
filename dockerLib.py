from os

def dockerInit(dockerName, fuzzingProgram, fuzzerName, dockerRepo, hostIP):
	os.system("docker pull %s:latest" % dockerRepo)
	os.system("docker run -d --privileged --name %s %s './start.sh %s %s %s %s'" % (dockerName, dockerRepo, fuzzerName, fuzzingProgram, hostIP, alias))