import os

def dockerRun(dockerName, fuzzingProgram, fuzzerName, dockerRepo, hostIP):
	os.system("docker pull %s:latest" % dockerRepo)
	os.system("docker run -dit --privileged --name %s %s /bin/sh -c './start.sh %s %s %s %s'" % (dockerName, dockerRepo, fuzzerName, fuzzingProgram, hostIP, dockerName))

def dockerStop(dockerName):
	os.system("docker stop %s" % dockerName)
	os.system("docker rm %s" % dockerName)
