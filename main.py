import time
import os
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

def print_colored_text(text, colors):
    for i, char in enumerate(text):
        print(colors[i % len(colors)] + char, end='', flush=True)
        time.sleep(0.05)  
    print()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    

    ascii_art = pyfiglet.figlet_format("ICARUS TWITCH BOT !")
    print(Fore.LIGHTBLUE_EX + ascii_art)
    
    print(Fore.YELLOW + "This is an adversite app not real software! If you wanna contact with us come our discord server.\n")
    
    discord_url = "discord.gg/icarus"
    print(Fore.CYAN + "Our Server: ", end="")
    
    colors = [Fore.MAGENTA]
    print_colored_text(discord_url, colors)

    print("\n" + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "We are waiting for u ")
    print(Fore.LIGHTWHITE_EX + "Press CTRL + C to exit.")
    
    while True:
        time.sleep(1)  

if __name__ == "__main__":
    main()


###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS
###### DISCORD.GG/ICARUS

