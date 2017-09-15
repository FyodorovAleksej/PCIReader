import os
import subprocess
subprocess.call("lspci -mm > " + os.getcwd() + "/log.txt", shell=True)
log = open(os.getcwd() + "/log.txt")
keys = ["id", "class", "vendorID", "deviceID", "rev"]
for i in log:
    ls = i.split(' "')
    if len(ls) > 1:
        a = {keys[j]: (ls[j][0:-1]) for j in range(0, len(keys))}
        print(a)
log.close()
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.getcwd() + "/log.txt")
os.remove(path)