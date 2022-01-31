⌄
⌄
⌄
⌄
import random, string
import webbrowser
import time
import requests
time.sleep(0.5)
print(""" 
█▀▀ █░░█ █▀▀ █▀▀ █░█ █▀▀ █▀▀█   █░░░█ █▀▀█ █░░ █▀▀ █▀▀ █▀▀▄
█░░ █▀▀█ █▀▀ █░░ █▀▄ █▀▀ █▄▄▀   █▄█▄█ █░░█ █░░ █▀▀ █▀▀ █░░█
▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ▀░▀ ▀▀▀ ▀░▀▀   ░▀░▀░ ▀▀▀▀ ▀▀▀ ▀░░ ▀▀▀ ▀▀▀░
█▀▀▄ █▀▀█ █▀▀█ █░█   █░░░█ █▀▀█ █░░ █▀▀
█░░█ █▄▄█ █▄▄▀ █▀▄   █▄█▄█ █░░█ █░░ █▀▀
▀▀▀░ ▀░░▀ ▀░▀▀ ▀░▀   ░▀░▀░ ▀▀▀▀ ▀▀▀ ▀░░""")
time.sleep(1.5)
print("My discord - https://discord.gg/ZxP7uken4Z")
time.sleep(1.5)
with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(" [WORK] | {} ".format(line.strip("\n")))
            break
        else:
        	print(" [BAD] | {} ".format(line.strip("\n")))
print("Script by 𝐃𝐚𝐫𝐤 𝐖𝐨𝐥𝐟 💎💦#0013")
