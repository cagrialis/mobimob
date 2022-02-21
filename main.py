import os
from colorama import *
import time
import threading
import sys

def writeName():

    name = f"""\
{Fore.CYAN}
   ▄▄▄▄███▄▄▄▄    ▄██████▄  ▀█████████▄   ▄█    ▄▄▄▄███▄▄▄▄    ▄██████▄  ▀█████████▄ 
 ▄██▀▀▀███▀▀▀██▄ ███    ███   ███    ███ ███  ▄██▀▀▀███▀▀▀██▄ ███    ███   ███    ███ 
 ███   ███   ███ ███    ███   ███    ███ ███▌ ███   ███   ███ ███    ███   ███    ███ 
 ███   ███   ███ ███    ███  ▄███▄▄▄██▀  ███▌ ███   ███   ███ ███    ███  ▄███▄▄▄██▀  
 ███   ███   ███ ███    ███ ▀▀███▀▀▀██▄  ███▌ ███   ███   ███ ███    ███ ▀▀███▀▀▀██▄  
 ███   ███   ███ ███    ███   ███    ██▄ ███  ███   ███   ███ ███    ███   ███    ██▄ 
 ███   ███   ███ ███    ███   ███    ███ ███  ███   ███   ███ ███    ███   ███    ███ 
  ▀█   ███   █▀   ▀██████▀  ▄█████████▀  █▀    ▀█   ███   █▀   ▀██████▀  ▄█████████▀   
                                                                {Style.RESET_ALL}v.1.0 https://github.com/cagrialis/mobimob
    """

    description = f"{Fore.RED}{Style.BRIGHT}Description : \n" \
                  f"{Style.RESET_ALL}MobiMob is a automatic scanning tool for android penetration test. \n" \
                  f"MobiMob has AndroBugs Framework, Androwarn and APKLeaks. \n" \
                  f"You can start these all tools with one command by using MobiMob. \n"

    print(name)
    print(description)

#NOW = datetime.utcnow().replace(microsecond=0)

def cdBack():
    os.system("cd ..")

def commandAndrobugs():
    commandStart = f"python ../AndroBugs_Framework/androbugs.py -f {sys.argv[1]} -o {sys.argv[2]}"
    os.system(commandStart)
    cdBack()

def commandAndrowarn():
    commandPip = "pip install -r ../androwarn/requirements.txt"
    commandStart = f"python3 ../androwarn/androwarn.py -i {sys.argv[1]} -o {sys.argv[2]}/androwarn.html -v 3"
    os.system(commandPip)
    os.system(commandStart)
    cdBack()

def commandApkleaks():
    commandPip = "pip install -r ../apkleaks/requirements.txt"
    commandStart = f"python3 ../apkleaks/apkleaks.py -f {sys.argv[1]} -o {sys.argv[2]}/apkleaks.json --json"
    os.system(commandPip)
    os.system(commandStart)
    cdBack()

if __name__ == '__main__':

    th1 = threading.Thread(target=writeName)
    th1.start()
    print(f"{Style.BRIGHT}MobiMob is starting... {Fore.MAGENTA}\"{sys.argv[1]}\"...{Style.RESET_ALL}\n")
    time.sleep(10)
    print(f"{Style.BRIGHT}AndroBugs Framework is starting... {Fore.MAGENTA}\"{sys.argv[1]}\"...{Style.RESET_ALL}\n")
    time.sleep(3)
    th2= threading.Thread(target=commandAndrobugs())
    th2.start()
    time.sleep(10)
    print(f"{Style.BRIGHT}Androwarn is starting... {Fore.MAGENTA}\"{sys.argv[1]}\"...{Style.RESET_ALL}\n")
    time.sleep(3)
    th3= threading.Thread(target=commandAndrowarn())
    th3.start()
    time.sleep(10)
    print(f"{Style.BRIGHT}Apkleaks is starting... {Fore.MAGENTA}\"{sys.argv[1]}\"...{Style.RESET_ALL}\n")
    time.sleep(3)
    th4= threading.Thread(target=commandApkleaks())
    th4.start()

