'''
дано ip set 142.108.56.118  maska 255.255.255.240 skolko v etoi seti ip adressov для которых
суммарное количество единиц в левых двух октетах менеьше чем суммарное количество единиц в правых?
'''
from ipaddress import *
net = ip_network('142.108.56.118/255.255.255.240',False)
kol= 0
for i in net:
    ip = f'{int(i):032b}'
    first = ip[:16]
    second = ip[16:]
    if first.count('1') < second.count('1'):
        kol+=1
print(kol)