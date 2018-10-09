#Command line argument
import sys

#command line arguments can be received using argv
#argv is a list. and all the arguments are String
print(len(sys.argv))

with open('ip.txt') as f:
    lines = f.readlines()

for x in lines:
	#x=x.split('\n') if ip's are entered line by line
	x=x.split(' ')
	
	
	if sys.argv[1]==x[0]:
		print ("ip found")
		sys.exit()
	else:
		print ("ip not found")

		

