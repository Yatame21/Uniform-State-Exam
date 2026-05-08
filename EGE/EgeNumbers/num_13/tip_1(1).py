'''
дано ip set 172.16.168.0  maska 255.255.248.0 skolko v etoi seti ip adressov для которых
количество единиц
в двоичной сети не кратко 5?
'''
from ipaddress import *
net =ip_network('172.16.168.0/255.255.248.0',False)
kol = 0
for i in net:
    ip = f'{int(i):032b}'
    if ip.count('1')% 5 != 0:
        kol+=1
print(kol)