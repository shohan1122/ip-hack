#coded by SHOHAN

#modules required
import argparse
import requests, json
import sys
from sys import argv
import os

#arguments and parser

parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
print (red+"""
█
    '\033[91;1m'      _____                    _____                            _____                    _____                    _____                    _____          
    '\033[912;1m'     /\    \                  /\    \                          /\    \                  /\    \                  /\    \                  /\    \         
     '\033[93;1m'   /::\    \                /::\    \                        /::\____\                /::\    \                /::\    \                /::\____\        
  '\033[94;1m'      \:::\    \              /::::\    \                      /:::/    /               /::::\    \              /::::\    \              /:::/    /        
  '\033[95;1m'       \:::\    \            /::::::\    \                    /:::/    /               /::::::\    \            /::::::\    \            /:::/    /         
    '\033[96;1m'      \:::\    \          /:::/\:::\    \                  /:::/    /               /:::/\:::\    \          /:::/\:::\    \          /:::/    /          
    '\033[97;1m'       \:::\    \        /:::/__\:::\    \                /:::/____/               /:::/__\:::\    \        /:::/  \:::\    \        /:::/____/           
 '\033[98;1m'          /::::\    \      /::::\   \:::\    \              /::::\    \              /::::\   \:::\    \      /:::/    \:::\    \      /::::\    \           
  '\033[94;1m'____    /::::::\    \    /::::::\   \:::\    \            /::::::\    \   _____    /::::::\   \:::\    \    /:::/    / \:::\    \    /::::::\____\________  
 '\033[95;1m'/\   \  /:::/\:::\    \  /:::/\:::\   \:::\____\          /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \  /:::/    /   \:::\    \  /:::/\:::::::::::\    \ 
'\033[91;1m'/::\   \/:::/  \:::\____\/:::/  \:::\   \:::|    |        /:::/  \:::\    /::\____\/:::/  \:::\   \:::\____\/:::/____/     \:::\____\/:::/  |:::::::::::\____\
'\033[97;1m'\:::\  /:::/    \::/    /\::/    \:::\  /:::|____|        \::/    \:::\  /:::/    /\::/    \:::\  /:::/    /\:::\    \      \::/    /\::/   |::|~~~|~~~~~     
 '\033[96;1m'\:::\/:::/    / \/____/  \/_____/\:::\/:::/    /          \/____/ \:::\/:::/    /  \/____/ \:::\/:::/    /  \:::\    \      \/____/  \/____|::|   |          
  '\033[93;1m'\::::::/    /                    \::::::/    /                    \::::::/    /            \::::::/    /    \:::\    \                    |::|   |          
 '\033[96;1m'  \::::/____/                      \::::/    /                      \::::/    /              \::::/    /      \:::\    \                   |::|   |          
 '\033[95;1m'   \:::\    \                       \::/____/                       /:::/    /               /:::/    /        \:::\    \                  |::|   |          
   '\033[92;1m'  \:::\    \                       ~~                            /:::/    /               /:::/    /          \:::\    \                 |::|   |          
      \:::\    \                                                   /:::/    /               /:::/    /            \:::\    \                |::|   |          
  '\033[97;1m'     \:::\____\                                                 /:::/    /               /:::/    /              \:::\____\               \::|   |          
        \::/    /                                                 \::/    /                \::/    /                \::/    /                \:|   |          
'\033[94;1m'         \/____/                                                   \/____/                  \/____/                  \/____/                  \|___|          
                                                                                                                                                              

                                                      v 1.0
"""+red)
print (lgreen+bold+"         <===[[ coded by SHOHAN ]]===> \n"+clear)
print (yellow+bold+"   <---(( search on youtube  technical Bangla ))--> \n"+clear)


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[Victim]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[ISP]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[Organisation]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[City]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Region]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Longitude]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Latitude]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Time zone]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[Zip code]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Terminating, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" check your internet connection!"+clear)
sys.exit(1)