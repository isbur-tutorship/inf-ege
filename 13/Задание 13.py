from ipaddress import ip_network
m = 0
net = ip_network('154.24.165.32/255.255.255.224', 0)
for ip in net:
    b = bin(int(ip)) [2:]
    bnet1 = b[:16]
    bnet2 = b[16:]
    if bnet1.count('1')<bnet2.count('1'):
        m = m+1