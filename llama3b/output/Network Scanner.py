# Network Scanner
import os
os.system("clear")
print("Network Scanner\n")
print("Enter an IP address on the network (192.168.0.1): ")
ip_range = input(">> ")
ip_addr = ip_range.split(".")
ip_start = 0
ip_end = 255
for last_octet in range(int(ip_start), int(ip_end) + 1):
    ip = ".".join(ip_addr[0:3]) + "." + str(last_octet)
    print("Pinging " + str(ip) + "...")
    try:
        os.system("ping -n 1 " + str(ip))
    except Exception as e:
        print("Error occurred while pinging:", e)
