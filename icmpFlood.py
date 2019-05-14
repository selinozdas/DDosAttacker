import ping3
import threading
ping3.DEBUG = True

def icmp_ping(number_of_packets,address):
    for i in range(0, number_of_packets):
        print(ping3.ping(address))


number_of_packets = 500

icmp_ping(number_of_packets,"randomweb.site")


