from __future__ import print_function  
import os
import random
numfiles = 10
good = random.randrange(numfiles)
print ("good: " + str(good))
for i in range(numfiles):
	f = open("message"+str(i)+".txt","w+")
	f.write (str(random.randrange(10000)))
	f.close()
	os.system("openssl dgst -sha512 -sign ./lab4_private.pem" + " -out ./message" + str(i) + ".txt.sign" + " message"+str(i)+".txt")
	f = open("message"+str(i)+".txt","r+")
	c = f.read(1)
	print (str(i) + ":" + str(c))
	f.seek(0,0)
	if i != good:
		f.write (str((int(c) + 1) % 10))
	f.close()


