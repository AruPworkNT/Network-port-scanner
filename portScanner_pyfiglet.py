import pyfiglet
import sys
import socket
from termcolor import colored
from datetime import datetime

front_banner=pyfiglet.figlet_format("PORT SCANNER")
print(colored(front_banner,'green'))

target=input(str("Target IP: "))
print(colored("Make sure that start port not grater then end port number\nAnd end port < 65535",'red'))
start_port=int(input("From which ports you want to start: "))
end_port=int(input("Enter you last port number where you want to stop scanning: "))

#Banner
print("_"*50)
print(colored("Scanning Taget: " + target,'green'))
print(colored("Scanning started at: " +str(datetime.now()),'green'))
print("_"*50) 

try:

    #scan port range on target ip
    for port in range(start_port,end_port):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        #return open port
        result=s.connect_ex((target,port))
        if result == 0:
            print("[*] Port{} is open".format(port))
        s.close

#error handling

except KeyboardInterrupt:
    print(colored("\n Exiting:(",'red'))
    sys.exit()

except socket.error:
    print(colored("\ Host not responding",'red'))

print(colored("Scan complete"))


input()
