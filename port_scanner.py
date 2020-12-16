#File Name     :port_scanner.py 
#Created by    : Dheeraj Deshmukh
#last modified : 16 Dec 2020
#python version: Python3.6 and above

import socket
from IPy import IP
import argparse
import pyfiglet

main_banner = pyfiglet.figlet_format("||..Port_Scanner..||")
print(main_banner)


parser = argparse.ArgumentParser()
parser.add_argument("-t","--target" ,help = "Enter Target Ip Or Domain...")
parser.add_argument("-sp","--sport",help = "Enter starting range for port number " ,type=int)
parser.add_argument("-cp","--cport",help = "Enter closeing range for port number " ,type=int)
parser.add_argument("-p","--port",help = "Enter range of port " ,type=int)



args = parser.parse_args()


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[* Scanning target]' + str(target))
    if args.cport and args.sport:
        for ports in range(args.sport,args.cport):
            scan_port(converted_ip,ports)
    if args.port:
        for ports in range(args.port):
            scan_port(converted_ip,ports)
def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)
def scan_port(ipaddress , port):
    try:
        sock = socket.socket()
        sock.settimeout(0.2)
        sock.connect((ipaddress , port))
        try:
            banner = get_banner(sock)
            print('[+] OPEN PORT ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] OPEN PORT ' + str(port))
    except:
        pass

targets = args.target
if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))
else:
    scan(targets)










