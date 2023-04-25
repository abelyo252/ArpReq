import time

import networkscan
import termcolor


# Main function
if __name__ == '__main__':
    print(termcolor.colored("[*] NetScanner", "green"))
    print("      : From the source")
    print("      : https://github.com/ericorain/python_scripts/tree/master/networkscan")
    print("")

    print("[!] Loading ...")
    time.sleep(5)

    a = termcolor.colored("       : Examples: 192.168.0.0/24, 172.16.1.128/28, etc. \n Please Enter [0] for exit ", "blue")


    while True :
        print("")

        EnterNetworkID = input(f"[+] Please Enter Network ID - 192.168.x.x/24  \n" + a + "\n# ")

        try:
            my_scan = networkscan.Networkscan(EnterNetworkID)

            # Display information
            print("Network to scan: " + str(my_scan.network))
            print("Prefix to scan: " + str(my_scan.network.prefixlen))
            print("Number of hosts to scan: " + str(my_scan.nbr_host))

            print("Scanning hosts...")
            my_scan.run()
            print("List of hosts found:")

            for i in my_scan.list_of_hosts_found:
                print(i)

            print("Number of hosts found: " + str(my_scan.nbr_host_found))

            res = my_scan.write_file()

            # Error while writting the file?
            if res:
                # Yes
                print("Write error with file " + my_scan.filename)

            else:
                # No error
                print("Data saved into file " + my_scan.filename)





        except :
            print(termcolor.colored("[!] Incorrect network / prefix", "red"))
            print(termcolor.colored("-----Please Enter Valid Network ID ", "red"))





