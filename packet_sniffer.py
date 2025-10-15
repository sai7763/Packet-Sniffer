from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def main():
    print("Starting packet capture... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, count=0)

if __name__ == "__main__":
    main()
