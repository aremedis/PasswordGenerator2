import random
import string
import sys


if sys.argv :
	rng = int(sys.argv[1])
else: rng = 34

print (''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(rng)]))