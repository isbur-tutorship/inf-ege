from ipaddress import ip_network

for i in range(0, 9):
    mask = "1" * i + "0" * (8-i)
    A = int(mask, 2)
    net = ip_network(f"243.46.4.198/255.255.{A}.0", strict=False)
    B = []
    for ip in net:
        ip = bin(int(ip))[2:]
        bin1 = ip[:16]
        bin2 = ip[16:]
        B.append(bin1.count("0") <= bin2.count("0"))
    if all(B):
        print(A)