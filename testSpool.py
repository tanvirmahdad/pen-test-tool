from metasploit.msfrpc import MsfRpcClient
from metasploit.msfconsole import MsfRpcConsole
import sys
import re
import socket
import time
import stdout

global global_positive_out
global_positive_out = list()
global global_console_status
global_console_status = True
global dataStore
global flag
flag=0

def read_console(console_data):
    global global_console_status
    global flag
    #global_console_status = console_data['busy']
   # print(console_data)
    sigdata = console_data['data'].rstrip().split('\n')
    for line in sigdata:
        if '[*] + [178.79.147.242] (178.79.147.242)' in line:
            flag=1
        if (flag==1):
            global_positive_out.append(line)
        if '[*] exec: whoami' in line:
            global_console_status=False
    print console_data['data']


client = MsfRpcClient('cloudSecurity')
console = MsfRpcConsole(client, cb=read_console)

console.execute('load wmap')
#console.execute('spool tanvir.txt')
console.execute('wmap_vulns -l')
console.execute('whoami')


while global_console_status:
    time.sleep(5)
global_positive_out.pop()
print(global_positive_out)
print(flag)
print(global_console_status)

try:
    console.console.destroy()
    print("Console Destroyed")

except:
    sys.exit()
