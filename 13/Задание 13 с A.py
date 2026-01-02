from ipaddress import ip_network

for A in range(0, 256):
    net = ip_network(f"159.242.{A}.0/255.255.254.0")
    B = []
    for ip in net:
        ip = bin(int(ip))[2:]
        bin1 = ip[:16]
        bin2 = ip[16:]
        B.append(bin1.count("0") < bin2.count("0"))
    if all(B):
        print(A)