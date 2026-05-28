from ipaddress import *

ipn = ip_network("150.122.11.21/255.255.254.0", 0)

print(bin(int(ipn[1])).count("1"))
