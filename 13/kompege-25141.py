from ipaddress import ip_network

net = ip_network("46.29.170.214/255.255.128.0", False)
for ip in net:
    octets = [int(x) for x in str(ip).split(".")]
    if max(octets) == sum(octets) - max(octets):
        print(ip)