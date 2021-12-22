import requests
import sys
from colorama import Fore, Back, Style, init
import os
import random 
from random import randint
import time
init(convert=True)

# -*- coding: ascii -*-

version = "3.0"
build = "22" 

counter = 1

characters = ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_abcdefghijklmnopqrstuvwxyz{|}'

def PrePairMSG(display, token, channel, message):
    
    headers = {"Authorization": token}

    try:
        msg_return = requests.post(f'https://discordapp.com/api/v7/channels/{channel}/messages', headers=headers, json={'content': message})
        if display == 1:
            if msg_return.status_code == 200:
                print(Fore.GREEN + f"[+] Message {counter} sent: {message}")
            else:
                print(Fore.RED + f"[-] Message {counter} could not be sent: {message}")
        
    except:
        print(Fore.RED + f"[-] Message {counter} could not be sent | Reason: Unknown")
def random_string(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))
   
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
        num_lines = sum(1 for line in open(file))
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
                    print(Fore.BLUE + "-"*85)
                    print()
                    print()
                    print(Fore.BLUE + f"[i] Messages sent: {counter}")
                    time.sleep(10)
                    print()
                    main()
            else:
                print(Fore.BLUE + "-"*85)
                print()
                print()
                print(Fore.BLUE + f"[i] Messages sent: {counter}")
                time.sleep(10)
                print()
                main()
    elif mode == 2:
        while counter <= msgsend:
            randomstring = ''
            for i in range(0, 75):
                randomstring += random.choice(characters)
            PrePairMSG(1, token, channel_id, randomstring)
            counter+=1
            randomstring = ""
            time.sleep(2.1)
        else:
            print(Fore.BLUE + "-"*85)
            print()
            print()
            print(Fore.BLUE + f"[i] Messages sent: {counter}")
            time.sleep(10)
            print()
            main()
            
            
if __name__ == '__main__':
    main()
