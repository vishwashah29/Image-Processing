import os
import time
import sys

#print(os.getcwd)
#os.mkdir("new_folder")
#time.sleep(5)
#os.rename('new_folder','new_folder2')
#time.sleep(3)
#os.rmdir('new_folder2')
#os.rmdir('new)folder2')


## working with sys module
sys.stderr.write('stderror print\n')
sys.stderr.flush()
sys.stdout.write('stdout Print\n')

print(sys.argv)

if len(sys.argv)>1:
    print((sys.argv[1]))
    
def printfunc(arg):
    print(arg)

printfunc(sys.argv[1])