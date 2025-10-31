from scapy.all import ARP, Ether, srp

while True:
    try:
        ip=input("Enter the target IP address or range here: ")
        if not ip:
            print("No IP address provided. Please try again.")
            continue
        elif ip.lower() in ['exit', 'quit']:
            print("Exiting the program.")
            break
        else:
            ether= Ether(dst="ff:ff:ff:ff:ff:ff")
            arp=ARP(pdst=ip)
            packet= ether/arp   

            result, noresult= srp(packet, timeout=3)
            print("Available hosts in the network:")

            for send, received in result:
                print(f"IP: {received[Ether].psrc} \t MAC: {received[Ether].hwsrc}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again.")
