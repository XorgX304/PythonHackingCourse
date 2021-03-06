import scapy.all as scapy
import optparse


def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    final_packet = broadcast/arp_req
    # answered, not_answered = scapy.srp(final_packet, timeout=1)
    answered = scapy.srp(final_packet, timeout=1, verbose=False)[0]

    template = "{0:8}  |  {1:10}"  # column widths:
    print (template.format("IP", "MAC Address"))  # header
    print("------------------------------")
    for element in answered:
        print(template.format(element[1].psrc,element[1].hwsrc))

    # to get the summary of a packet use : packet.summary() or packet.show()
    # to get more info use : scapy.ls(type)


def pars():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target ", dest="target", help="A single target or a subnet to be scanned")
    return parser.parse_args()


options, arguments = pars()
target = options.target
# ip = input("Please Enter IP address or a subnet to scan: ")
scan(target)
