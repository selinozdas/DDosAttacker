import ping3
import threading
from scapy.all import *
from spoof import ip_spoof

ping3.DEBUG = True

spoofedIP = ip_spoof()
c = RandShort()



print(spoofedIP)
def icmp_ping(number_of_packets,address):
    for i in range(0, number_of_packets):
        print(ping3.ping(address))


number_of_packets = 500

icmp_ping(number_of_packets,"randomweb.site")


