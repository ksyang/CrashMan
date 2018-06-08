import dockerLib

a = str(input())

if a == '1':
	dockerLib.dockerRun("ssgskid", "ijgjpeg", "afl", "ssgskid/afl-ijgjpeg", "http://35.200.9.22:30001", "dockerLibTest")
	exit()
if a == '2':
	dockerLib.dockerStop("ssgskid")
	exit()

print "invalid input!"
