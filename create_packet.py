from scapy.all import IP , ICMP , sr1


while True:
    try:
        dst=input("Enter the destination IP address: ")
        src=input("Enter the source IP address: ")
        dest_ip = IP(src=src, dst=dst, id=100)
        icmp_1= ICMP(id=1000)
        packet = dest_ip / icmp_1
        response = sr1(packet)
        if response:
            print("Received response from:", response.show())
        else:
            print("No response received.")
        ch = input("do you want to continue(y/n): ")
        if ch.lower() =='n' or ch.lower()=='no':
            print("GOOD BYE!")
            break
        else:
            continue
    except Exception:
        print("An error occurred. Please check the IP addresses and try again.")
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
        break 
