import os
import subprocess
#call linux shell command (lspci) with output in file "/log.txt" for getting all PCI devices
subprocess.call("lspci -mmnn > " + os.getcwd() + "/log.txt", shell=True)
#open temp file "/log.txt"
log = open(os.getcwd() + "/log.txt")
#create dictinory with information about vendorID and deviceID
keys = ["vendorID", "deviceID"]
for i in log:
    #parsing every column of information
    ls = i.split(' "')
    if len(ls) > 1:
        #generate dictinory with this information
        a = {keys[j]: (ls[j+2][0:-1]) for j in range(0, len(keys))}
        #editing the deviceID
        b = a['deviceID']
        l = b.split('"')
        a['deviceID'] = l[0]
        print(a)
log.close()
#remove temp file "/log.txt"
path = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.getcwd() + "/log.txt")
os.remove(path)