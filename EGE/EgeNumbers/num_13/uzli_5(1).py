"""
ДАНО ip et = 192.168.190.12 mask = 192.168.184.0
укажите наибольшее возможное количесвто единиц в маске этой сети
"""
from ipaddress import *
ip_1 = ip_address("192.168.190.12")
ip_2 = ip_address('192.168.184.0')
for mask in range (31)[::-1]:
    net_1 = ip_network(f'{ip_1}/{mask}',False) # так же в любом другом можно вместо false просто 0 писать lol
    net_2 = ip_network(f'{ip_2}/{mask}', False)
    if net_1 == net_2 and ip_1 in net_1.hosts() and ip_2 in net_2.hosts():
        print(mask)
        break