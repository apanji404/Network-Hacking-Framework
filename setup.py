import pyfiglet
import sys, os
import re
import urllib.request  as urllib2 

H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'

def desc():
	print(F+'''
    This program was created for review and not for causing harm.
    Usage of framework for attacking targets without prior mutual consent is illegal.
    Developers assume no liability and are not responsible for any misuse or damage caused by this program.
    '''+E)

ascii_banner = pyfiglet.figlet_format("WELCOME")
print(ascii_banner)

def main_menu():
    desc()
    print('\n')
    print(B+'''
	Menu Scanning:
  	'''+E+'''
  	1) Network Scanning
  	2) Port Scanning
  	'''+W+'''-------------------'''+E)
    print(B + '''
  	Menu Pentest:
  	'''+E+'''
  	3) Sniffing 
  	5) ARP Spoof
  	6) DNS Spoof
        7) Exploit
  	'''+W+'''-------------------\n'''+E)
    try:
        v = input('Choose-»')
    except:
        print(' Good by ')
        exit()

main_menu()
