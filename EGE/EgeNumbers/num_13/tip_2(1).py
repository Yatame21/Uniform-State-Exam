'''
дано ip узел 192.168.24.72
сеть = 192.168.24.64
определите наименьшее возможное количество единиц
в последних двух байтах маски
'''

from ipaddress import *
ip_host = ip_address('192.168.24.72')
ip_net = ip_address('192.168.24.64')
bit_mask = []
for mask in range(17,31):
    net= ip_network(f'{ip_host}/{mask}',False)
    if ip_host in net.hosts() and net.network_address == ip_net:
        bit_mask.append(f"{int( net.netmask):032b}"[16:])
print(min(bit_mask).count('1'))

