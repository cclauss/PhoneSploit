# coding: latin-1

#Coded By Zucccs
# Enjoy


#=============================
#Imports
import os
import random
import time as  t
from colorama import Fore, init

#=============================
# Variables
CurrentDir = os.path.dirname(os.path.abspath(__file__))
load_count = 0

#=============================
#Install Functions
# def ColoringModeStartup():
#     coloring_file = open(CurrentDir+"\\install\\coloring.txt", "a+")
#     line = open(CurrentDir+"\\install\\coloring.txt", "a+").readline()
#     if 'init' in line:
#         init(convert=True)
#         main()
#     if 'false' in line:
#         main()
#     if "NOT_LOADED" in line:
#         platform_choice = raw_input("Are you loading this script in (W)indows or (L)inux: ")
#         open(CurrentDir+"\\install\\coloring.txt", "w").close()
#         if platform_choice.lower() == 'w':
#             coloring_file.write("init")
#         else:
#             coloring_file.write("false")
#             yn = raw_input(Fore.WHITE + "Have you already installed adb via command line "+Fore.GREEN + "Y"+Fore.WHITE+"/"+Fore.RED+"N "+Fore.WHITE)
#             if yn == "n":
#                 os.system("sudo apt install adb")
#             else:
#                 main()

#=============================
# Graphics # http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

arrow = Fore.RED + " └──>".decode("utf-8") + Fore.WHITE
connect = Fore.RED + "│".decode("utf-8") + Fore.WHITE

logo_design_1 = ('''
  {0}  ____  __                    _____       __      _ __ 
   / __ \/ /_  ____  ____  ___ / ___/____  / /___  (_) /_
  / /_/ / __ \/ __ \/ __ \/ _ \\__ \/ __ \/ / __ \/ / __/
{1} / ____/ / / / /_/ / / / /  __/__/ / /_/ / / /_/ / / /_  
/_/   /_/ /_/\____/_/ /_/\___/____/ .___/_/\____/_/\__/  
                                 /_/''').format(Fore.GREEN, Fore.WHITE, Fore.RED)

logo_design_2 = Fore.GREEN + '''                                             
  .;'                     `;,
 .;'  ,;'             `;,  `;,   {0}PhoneSploit
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   {1}( ){0}   :   ::   ::  {1}Coded by Zucccs / Metachar{0}
':.  ':.  ':. {1}/_\{0} ,:'  ,:'  ,:'
 ':.  ':.    {1}/___\{0}    ,:'  ,:'   
  ':.       {1}/_____\{0}      ,:'
           {1}/       \\{0}
'''.format(Fore.GREEN, Fore.WHITE, Fore.RED)

logo_design_pre = '''
{0}╔═╗{1}┬ ┬┌─┐┌┐┌┌─┐{0}╔═╗{1}┌─┐┬  ┌─┐┬┌┬┐
{0}╠═╝{1}├─┤│ ││││├┤ {0}╚═╗{1}├─┘│  │ ││ │ 
{0}╩  {1}┴ ┴└─┘┘└┘└─┘{0}╚═╝{1}┴  ┴─┘└─┘┴ ┴ '''.format(Fore.GREEN, Fore.WHITE, Fore.RED)
logo_design_3 = logo_design_pre.decode("utf-8")

logo_design_4 = '''
\033[92m
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..              \033[0m Expoit time :) \033[92m
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.            \033[0m Thanks for downloading!\033[92m
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs'''

message = '''\n
{0}[{1}1{0}] {2}Show Connected Devices      {0}[{1}6{0}] {2}Screen record a phone               {0}[{1}11{0}] {2}Uninstall an app                   {0}[{1}16{0}]{2} Port Forwarding
{0}[{1}2{0}] {2}Disconect all devices       {0}[{1}7{0}] {2}Screen Shot a picture on a phone    {0}[{1}12{0}] {2}Show real time log of device
{0}[{1}3{0}] {2}Connect a new phone         {0}[{1}8{0}] {2}Restart Server                      {0}[{1}13{0}] {2}Dump System Info
{0}[{1}4{0}] {2}Access Shell on a phone     {0}[{1}9{0}] {2}Pull folders from phone to pc       {0}[{1}14{0}] {2}List all apps on a phone
{0}[{1}5{0}] {2}Install an apk on a phone   {0}[{1}10{0}] {2}Turn The Device off                {0}[{1}15{0}] {2}Run an app


{0}[{1}99{0}] {2}Exit   {0}[{1}0{0}] {2}Clear
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN)
#=============================
#Main
def main():
    option = raw_input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")
    if option == '1':
            os.system("adb devices -l")
    elif option  ==  '2':
        os.system("adb disconnect")
    elif option == '3':
        print ("\n[{0}+{1}] Enter a phones ip address.").format(Fore.RED, Fore.WHITE)
        ip = raw_input (arrow+" phonesploit"+Fore.RED + "(connect_phone) "+Fore.WHITE + "> ")
        os.system("adb connect "+ip+":5555")
    
    elif option  == '4':
        print ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(shell_on_phone) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" shell")

    elif option == '5':
        print  ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(apk_install) "+Fore.WHITE + "> ")
        print ("     "+connect)
        print  ("    [{0}+{1}]Enter the apk location.").format(Fore.RED, Fore.WHITE)
        apk_location = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(apk_install) "+Fore.WHITE + "> ")
        os.system("adb -s  "+device_name+" install "+apk_location)
        print (Fore.GREEN  +  "Apk has been installed.")

    elif option ==  '6':
        print  ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(screen_record) "+Fore.WHITE + "> ")
        print ("     "+connect)
        print ("    [{0}+{1}] Please wait 3m its recording").format(Fore.RED, Fore.WHITE)
        print ("     "+connect)   
        os.system("adb -s "+device_name+" shell screenrecord /sdcard/demo.mp4")
        print  ("    [{0}+{1}]Enter where you would like the video to be saved.").format(Fore.RED, Fore.WHITE) 
        place_location = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(screen_record) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" pull /sdcard/demo.mp4 "+place_location)

    elif option  == '7':
        print  ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(screenshot) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" shell screencap /sdcard/screen.png")
        print("     "+connect)
        print  ("    [{0}+{1}]Enter where you would like the screenshot to be saved.").format(Fore.RED, Fore.WHITE)
        place_location = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(screenshot) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" pull /sdcard/screen.png "+place_location)

    elif option == '8':
        os.system("adb kill-server && adb start-server")
    
    elif option == '9':
        print  ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(file_pull) "+Fore.WHITE + "> ")
        print("     "+connect)
        print ("    [{0}+{1}]Enter a file location on a device").format(Fore.RED, Fore.WHITE)
        file_location = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(file_pull) "+Fore.WHITE + "> ")
        print("        "+connect)
        print ("       [{0}+{1}]Enter where you would like the file to be saved.").format(Fore.RED, Fore.WHITE)
        place_location = raw_input("       "+arrow + "phonesploit"+Fore.RED + "(file_pull) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" pull "+file_location+" "+place_location)

    elif option == '10':
        print  ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(device_reboot) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+ " reboot ")
    
    elif option ==  '11':
        print  ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(app_delete) "+Fore.WHITE + "> ")
        print("     "+connect)
        print  ("    [{0}+{1}]Enter a package name.").format(Fore.RED, Fore.WHITE)
        package_name = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(app_delete) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" unistall "+package_name)

    elif option == '12':
        print  ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(log) "+Fore.WHITE + "> ")
        os.system('adb -s '+device_name+" logcat ")

    elif option == '13':
        print  ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(sys_info) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" dumpsys")        

    elif option == '14':
        print  ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(package_manager) "+Fore.WHITE + "> ")
        os.system("adb -s " +device_name+ " shell pm list packages -f")
        main()

    elif option == '15':
        print  ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(app_run) "+Fore.WHITE + "> ")
        print("     "+connect)
        print  ("    [{0}+{1}]Enter a package name. They look like this --> com.snapchat.android").format(Fore.RED, Fore.WHITE)
        package_name = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(app_run) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" shell monkey -p "+package_name+" -v 500")
        main()      

    elif option == '16':
        print  ("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE)
        device_name = raw_input(arrow + "phonesploit"+Fore.RED + "(port_forward) "+Fore.WHITE + "> ")
        print("     "+connect)
        print  ("    [{0}+{1}]Enter a port on the device.").format(Fore.RED, Fore.WHITE)
        port_device = raw_input("    "+arrow + "phonesploit"+Fore.RED + "(port_forward) "+Fore.WHITE + "> ")
        print("         "+connect)       
        print  ("        [{0}+{1}]Enter a port to forward it too.").format(Fore.RED, Fore.WHITE)
        forward_port = raw_input("        "+arrow + "phonesploit"+Fore.RED + "(port_forward) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" forward tcp:"+port_device+" tcp:"+forward_port) 

    elif option  == '0':
        os.system('clear')
        banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4])
        print Fore.RED + banner_title  
        print message

    elif option == '99':
        exit()


    main()



#=============================
# Run
yn = raw_input(Fore.WHITE + "Have you already installed adb via command line "+Fore.GREEN + "Y"+Fore.WHITE+"/"+Fore.RED+"N "+Fore.WHITE)
if yn == "n":
    os.system("sudo apt install adb")
print (Fore.RED + "Starting  adb server..")
os.system("adb tcpip 5555")
t.sleep(4)
os.system('clear')
banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4])
print Fore.RED + banner_title  
print message
main()
