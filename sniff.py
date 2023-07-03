from time import sleep
from scapy.all import *

iface = 'wlan0mon'
devices = set()

def dump_packet(pkt):
    if not pkt.haslayer(Dot11Beacon) and not pkt.haslayer(Dot11ProbeReq) and not pkt.haslayer(Dot11ProbeResp):
        print(pkt.summary())
    if pkt.haslayer(Raw):   
        print(hexdump(pkt.load), "\n")

while True:
    sleep(0.01)
    sniff(iface=iface, prn=dump_packet, count=10, timeout=5, store=0)
