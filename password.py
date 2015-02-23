import random
import string
import sys

# print (len(sys.argv))

if len(sys.argv) < 2 :
	print ("Given Length is too short, setting password length to 34")
	rng = 34
else: rng = int(sys.argv[1])

print (''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(rng)]))


# Things to add in the future:
# -a way to exclude certain characters
# -a way to check for duplicate characters, and allow for no duplicates