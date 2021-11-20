import requests
import sys
from colorama import Fore, Back, Style, init
import os
import random 
import time
init(convert=True)

msgid = 0
max_length = 75
characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'

class PrePairMSG:
    
    def __init__(self, token, channel, message):
        self.token = token
        self.channel_id = channel
        self.message = message
        self.headers = {"Authorization": token}

    def _generate_message(self, m1):
        return m1


    def execute(self):
        return requests.post(f'https://discordapp.com/api/v9/channels/{self.channel_id}/messages', headers=self.headers, json={'content': self._generate_message(self.message)})

def random_string(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))
   
def clear():

    print() * 150
    
def main():

    num_lines = sum(1 for line in open('words.txt'))
    print(Fore.CYAN + "-"*50)
    print(Fore.CYAN + "Script made by: Levi2288 | Advanced discord spammer")
    print(Fore.CYAN + "-"*50)
    print()
    print(Fore.RED + "Modes: 1 = read messages from word list | 2 = random strings")
    print(Style.RESET_ALL)
    print()
    mode = int(input("Msg mode:"))
    token = input("Token:")
    channel_id = int(input("Channel ID:"))
    if mode == 1:
        print()
        print(Fore.RED + f"If you are using Msg mode 1 your max messages cant be more then \"{num_lines}\"")
        print(Style.RESET_ALL)
        msgsend =  int(input("Messages to send (number):"))
    elif mode == 2:
        msgsend =  int(input("Messages to send (number):"))
    print(Style.RESET_ALL)
    print()
    print()
    print(Fore.GREEN + f"Token: {token}")
    print(Fore.GREEN + f"ChannelID: {channel_id}")
    print(Fore.GREEN + f"Messages to send: {msgsend}")
    print()
    print(Fore.GREEN + f"Start in 3 seconds")
    time.sleep(3)
    
    counter = 0
    if mode == 1:
        with open("words.txt", "r") as a_file:
            for line in a_file:
                if counter < msgsend :
                    message = line.strip()
                    epicness = PrePairMSG(token, channel_id, message)
                    epicness.execute()
                    print(Fore.GREEN + f"Message sent: {message} | {channel_id}")
                    time.sleep(2.1)
                    counter+=1
                else:
                    print()
                    print()
                    print(Fore.BLUE + f"Messages sent: {counter}")
                    time.sleep(10)
                    main()
            else:
                print()
                print()
                print(Fore.BLUE + f"Messages sent: {counter}")
                time.sleep(10)
                main()
    elif mode == 2:
        while counter <= msgsend:
            randomstring = ''
            for i in range(0, 75):
                randomstring += random.choice(characters)
            epicness = PrePairMSG(token, channel_id, randomstring)
            epicness.execute()
            print(f"Message sent: {randomstring} | {channel_id}")
            randomstring = ""
            time.sleep(2.1)
            counter+=1
        else:
            print()
            print()
            print(Fore.BLUE + f"Messages sent: {counter}")
            time.sleep(10)
            main()
if __name__ == '__main__':
    main()
