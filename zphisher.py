def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
        
        
        
import os
import time
import sys

os.system("clear")

os.system("pkg install tur-repo")

os.system("pkg install zphisher")

os.system("git clone --depth=1 https://github.com/htr-tech/zphisher.git")


os.system("cd zphisher")

os.system("clear")



slowprint('''\033[91m
           __  __           _   _   _            _
          |  \/  | __ _  __| | | | | | __ _  ___| | ___ __
          | |\/| |/ _` |/ _` | | |_| |/ _` |/ __| |/ / '__|
          | |  | | (_| | (_| | |  _  | (_| | (__|   <| |
          |_|  |_|\__,_|\__,_| |_| |_|\__,_|\___|_|\_\_|
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

slowprint('''\033[95m
            +--------------------------------------+
            |         This Tool for zphisher       |
            +--------------------------------------+
            | Coded By Mad Hackr | version :  2.0  |
            +--------------------------------------+''')


print ("                                            ")
choice = input("\033[93m Do You Want to Nexphisher [N/Y] : ")
if choice == 'N' : os.system ("exit")
if choice == 'Y' : os.system ("bash zphisher.sh")