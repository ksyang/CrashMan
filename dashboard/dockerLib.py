import sys

def dockerInit(dockerName, fuzzingProgram, fuzzerName, dockerRepo, hostIP):
	os.system("docker pull %s:latest" % dockerRepo)
	os.system("docker run -d -i --name %s %s './start.sh;python CrashMan_client/sender/sender.py /tmp/outputs/crashes %s %s %s'" % (dockerName, dockerRepo, fuzzerName, fuzzingProgram, hostIP))
