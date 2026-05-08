"""
ДАНО ip et = 127.0.1.65 mask = 127.0.1.101
укажите наименьшее возможное количесвто адресов этой сети
"""
from ipaddress import *
ip_1 = ip_address("127.0.1.65")
ip_2 = ip_address('127.0.1.101')
k = []
for mask in range(31)[::-1]:
    net_1 = ip_network(f'{ip_1}/{mask}',False) # так же в любом другом можно вместо false просто 0 писать lol
    net_2 = ip_network(f'{ip_2}/{mask}', False)
    if net_1 == net_2 and ip_1 in net_1.hosts() and ip_2 in net_1.hosts():
        print(net_1.num_addresses)
        break