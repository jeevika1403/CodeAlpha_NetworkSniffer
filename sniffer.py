from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime

def packet_handler(packet):
    if IP in packet:
        print("\n================ PACKET CAPTURED ================")
        print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        if TCP in packet:
            print("Protocol: TCP")
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)
            payload = bytes(packet[TCP].payload)
            if payload:
                print("Payload:", payload)
            else:
                print("Payload: None")

        elif UDP in packet:
            print("Protocol: UDP")
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)
            payload = bytes(packet[UDP].payload)
            if payload:
                print("Payload:", payload)
            else:
                print("Payload: None")

        elif ICMP in packet:
            print("Protocol: ICMP")
            payload = bytes(packet[ICMP].payload)
            if payload:
                print("Payload:", payload)
            else:
                print("Payload: None")

        print("=================================================")

print("Starting Basic Network Sniffer...")
print("Capturing Source IP, Destination IP, Protocol, Payload")
print("Generate traffic by pinging or browsing\n")

sniff(prn=packet_handler, store=False)
