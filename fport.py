import os,sys
import subprocess
import re,time

um="usage: python fport.py google.com -p80"

command=["nmap"]
opentimes=[]

try:
	wait=int(sys.argv[1])
	delay=int(sys.argv[2])
	sl=3
except:
	wait=1
	delay=10
	sl=1

try:
  for i in range(sl,len(sys.argv)):
	command.append(sys.argv[i])
except:
  print um


for i in range(1,int(delay)+1):
	out=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	line=out.stdout.readlines()
	for i in line:
	    if list(i)[0]!="#":
                print i[:-1]
		m=re.findall("/closed/|/open/",i)
		
		if m==["/open/"]:
			opentimes.append(time.ctime())
		
	
	print "-----------------------------------------------------------------------"
	time.sleep(int(wait))

if len(opentimes)>=1:
	print "Open times :\n"
	for i in opentimes:
		print i

