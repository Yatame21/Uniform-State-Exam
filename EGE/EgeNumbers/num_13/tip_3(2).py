"""
ДАНО ip et = 255.215.88.80 mask = 255.255.A.0
определите минимальное значение А для которого для всех айпи адресов сети в двоичной записи
айпи адреса суммарное количество нулей в левых двух байтах НЕ БОЛЕЕ суммарного количества НУЛЕЙ
единиц в правых двух байтах
"""


from ipaddress import *
ip_net = ip_address('255.215.88.80')
for A in range(16,24):
    net = ip_network(f"{ip_net}/{A}",False)

    if all(f"{int(ip):032b}"[:16].count('0')<=f"{int(ip):032b}"[16:].count('0') for ip in net):
        res_mask = str(net.netmask).split('.')
        print(res_mask[2])
        break


