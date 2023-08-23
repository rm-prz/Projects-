import sys
import socket
from datetime import datetime

#user inserts IP address
IP = input(str("Your IP Address: "))

print("_" * 50)
print("Scanning Target: " + IP)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

#scans for common ports
common_ports = [21,22,23,25,53,80,110,443,3306]


try:
    #finds ports
    for port in common_ports:
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #searches for ports
        result = s.connect_ex((IP,port))

        #displays port if open
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting :(")
    sys.exit()
except socket.error:
    print("\ Host not responding :(")
    sys.exit()
               
