import requests
import sys
from colorama import Fore, Back, Style, init
import os
import random 
from random import randint
import time
init(convert=True)

sucess = 0
failed = 0
counter = 1
# -*- coding: ascii -*-

version = "3.0 DEV"
build = "27" 


characters = ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}'

def PrePairMSG(display, token, channel, message):
    
    global sucess
    global failed
    headers = {"Authorization": token}

    try:
        msg_return = requests.post(f'https://discordapp.com/api/v9/channels/{channel}/messages', headers=headers, json={'content': message})
        if display == 1:
            if msg_return.status_code == 200:
                print(Fore.GREEN + f"[+] Message {counter} sent: {message}")
                sucess+=1
            elif msg_return.status_code == 404:
                print(Fore.RED + f"[-] Message {counter} could not be sent | Reason: Not Found")
                failed+=1
            else:
                print(Fore.RED + f"[-] Message {counter} could not be sent | Reason: Unknown")
                failed+=1
        
    except:
        print(Fore.RED + f"[-] Message {counter} could not be sent | Reason: Unknown")
def random_string():
   return ''.join(random.choice(characters) for i in range(0, random.randint(6,75)))

def job_done():

    print(Fore.BLUE + "-"*85)
    print()
    print()
    print(Fore.BLUE + f"[i] Job: Finished")
    print(Fore.BLUE + f"[i] Messages sent: {sucess}")
    print(Fore.BLUE + f"[i] Errors: {failed}")
    time.sleep(10)
    print()
    main()
    
    
def start_add(token, channel_id):

    start_msg = randint(1, 5)
    if start_msg == 1:
        PrePairMSG(0, token, channel_id, "Advanced Dc spammer starting... Made by: Levi2288")
        
    elif start_msg == 2:
        PrePairMSG(0, token, channel_id, "Ladies and gentlemen Advanced spammer. Still on top")
        
    elif start_msg == 3:
        PrePairMSG(0, token, channel_id, "Be the best or cry like the rest. Advanced DC spammer")
        
    elif start_msg == 4:
        PrePairMSG(0, token, channel_id, "No im not using Advanced DC spammer, i can just type at lightspeed :smirk:")
        
    elif start_msg == 5:
        PrePairMSG(0, token, channel_id, "Still #1 | Advanced spammer")
        
    time.sleep(2.1)
    PrePairMSG(0, token, channel_id, f"---------------Version: {version} | Build: {build}---------------")
    time.sleep(1)
   
 
def main():
    global counter
    global sucess
    global failed
    
    counter = 1
    sucess = 0
    failed = 0
    
    print(Fore.CYAN + "-"*85)
    print(Fore.CYAN + f" ██████╗  ██████╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗\n ██╔══██╗██╔════╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗\n ██║  ██║██║         ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝\n ██║  ██║██║         ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗\n ██████╔╝╚██████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║\n ╚═════╝  ╚═════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═")
    print(Fore.CYAN + "Script made by: Levi2288 | Advanced discord spammer")
    print(Fore.CYAN + "-"*85)
    print()
    print(Fore.RED + "Modes: 1 = read messages from word list | 2 = random strings")
    print(Style.RESET_ALL)
    print()
    mode = int(input("Msg mode:"))
    token = input("Token:")
    channel_id = int(input("Channel ID:"))
    if mode == 1:
        file = input("File With the Worlds:")
        num_lines = 0
        with open(file) as infp:
            for line in infp:
                if line.strip():
                    num_lines += 1
        #num_lines = sum(1 for line in open(file))
        print()
        print(Fore.RED + f"If you are using Msg mode 1 your max messages cant be more then \"{num_lines}\"")
        print(Style.RESET_ALL)
        msgsend =  int(input("Messages to send (number):"))
        print()
        print(Fore.RED + f"File name or path. Example: (words.txt)")
        print(Style.RESET_ALL)
    elif mode == 2:
        msgsend =  int(input("Messages to send (number):"))
    
    
    print(Style.RESET_ALL)
    print()
    print()
    print(Fore.BLUE + f"Token: {token}")
    print(Fore.BLUE + f"ChannelID: {channel_id}")
    print(Fore.BLUE + f"Messages to send: {msgsend}")
    print()
    print(Fore.BLUE + f"Start in 3 seconds")
     
    start_add(token, channel_id)
    if mode == 1:
        with open(file, "r") as a_file:
            for line in a_file:
                if counter < msgsend :
                    message = line.strip()
                    if(len(message) > 0):
                        PrePairMSG(1, token, channel_id, message)
                        counter+=1
                        time.sleep(2.1)
                    else:
                        print(Fore.RED + f"[-] Empty String! Skipping...")
                else:
                    job_done()
            else:
               job_done()
    elif mode == 2:
        while counter <= msgsend:
            randomstring = ''
            #for i in range(0, 75):
            #    randomstring += random.choice(characters)
            randomstring = random_string()
            PrePairMSG(1, token, channel_id, randomstring)
            counter+=1
            randomstring = ""
            time.sleep(2.1)
        else:
            job_done()
            
            
if __name__ == '__main__':
    main()
