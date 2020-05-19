#Jamison Wilkes#IPLab

import ipaddress

#1 
print('#1 What is the first address of a block of classless addresses if one of the addresses is 192.168.2.76/28?')
ipInterface = ipaddress.ip_interface('192.168.2.76/28')
ipNetwork = ipInterface.network
networkAddress = ipaddress.ip_network(ipNetwork).network_address
print('Network Address = {}'.format(networkAddress))
print('First Usable Address = {}'.format(networkAddress + 1))

#2
print('#2 What is the first address of a block of classless addresses if one of the addresses is 192.168.2.76/9?')
ipInterface = ipaddress.ip_interface('192.168.2.76/9')
ipNetwork = ipInterface.network
networkAddress = ipaddress.ip_network(ipNetwork).network_address
print('Network Address = {}'.format(networkAddress))
print('First Usable Address = {}'.format(networkAddress + 1))

#3
print('#3 What is the first address of a block of classless addresses if one of the addresses is 192.168.2.137/27?')
ipInterface = ipaddress.ip_interface('192.168.2.137/27')
ipNetwork = ipInterface.network
networkAddress = ipaddress.ip_network(ipNetwork).network_address
print('Network Address = {}'.format(networkAddress))
print('First Usable Address = {}'.format(networkAddress + 1))

#4
print('#4Find the number of addresses in a block of classless addresses if one of the addresses is 101.10.2.8/15')
ipInterface = ipaddress.ip_interface('101.10.2.8/15')
ipNetwork = ipInterface.network
networkAddress = ipaddress.ip_network(ipNetwork).network_address
print('Total Addresses: {}'.format(len(list(ipNetwork.hosts()))))
print('Usable Addresses: {}'.format((networkAddress)))

#5
print('#5Find the number of addresses in a block of classless addresses if one of the addresses is 101.10.2.8/29')
ipInterface = ipaddress.ip_interface('101.10.2.8/29')
ipNetwork = ipInterface.network
networkAddress = ipaddress.ip_network(ipNetwork).network_address
print('Total Addresses: {}'.format(len(list(ipNetwork.hosts()))))
print('Usable Addresses: {}'.format(networkAddress))

#6
print('#6What is the last address of a block of classless addresses if one of the addresses is 192.168.2.137/27?')
ipInterface = ipaddress.ip_interface('192.168.2.137/27')
ipNetwork = ipInterface.network
networkAddress = ipaddress.ip_network(ipNetwork).network_address
print('Broadcast Address = {}'.format(ipNetwork.broadcast_address))
print('Last Usable Address = {}'.format(ipNetwork.broadcast_address - 1))

#7
print('#7What is the last address of a block of classless addresses if one of the addresses is 110.10.2.55/30?')
ipInterface = ipaddress.ip_interface('110.10.2.55/30')
ipNetwork = ipInterface.network
networkAddress = ipaddress.ip_network(ipNetwork).network_address
print('Broadcast Address = {}'.format(ipNetwork.broadcast_address))
print ('Last Usable Address = {}'.format(ipNetwork.broadcast_address - 1))

#8
print('#8An organization is granted a block; one address is 110.10.10.64/20. The organization needs 10 subnets. What is the subnet prefix length?')
ipInterface = ipaddress.ip_interface('110.10.10.64/20')
ipNetwork = ipInterface.network
networkAddress = ipaddress.ip_network(ipNetwork).network_address
print('Subnet Prefix Length = {}'.format(ipNetwork.prefixlen))

#9
print('#9An organization is granted a block; one address is 110.10.10.64/25. If the subnet prefix length is /28, what is the maximum number of subnets and how many addresses in each subnet?')
ipInterface = ipaddress.ip_interface('110.10.10.64/25')
ipNetwork = ipInterface.network
networkAddress = ipaddress.ip_network(ipNetwork).network_address
print('{}'.format(len(list(ipNetwork.subnets(new_prefix=28)))) + 'subnets with {}'.format(len(list(ipNetwork.subnets()))) +'addresses in each subnet')

#10
print('#10an organization is granted a block of classless addresses with one of the addresses: 156.78.51.24/25. how many addresses are granted?')
ipinterface = ipaddress.ip_interface('156.78.51.24/25')
ipnetwork = ipinterface.network
networkAddress = ipaddress.ip_network(ipnetwork).network_address
print('total addresses = {}'.format(len(list(ipNetwork.hosts()))))

#11
print('#11 An organization is granted a block of classless addresses with one of the addresses: 156.78.51.24/30. How many addresses are granted?')
ipInterface = ipaddress.ip_interface('156.78.51.24/30')
ipNetwork = ipInterface.network
networkAddress = ipaddress.ip_network(ipNetwork).network_address
print('Total Addresses = {}'.format(len(list(ipNetwork.hosts()))))

 #12
print('#12 An organization is granted a block of classless addresses with one of the addresses: 166.25.132.0/3. How many addresses are granted?')
ipInterface = ipaddress.ip_interface('166.25.132.0/3')
ipNetwork = ipInterface.network
networkAddress = ipaddress.ip_network(ipNetwork).network_address
print('Total Addresses = {}'.format(len(list(ipNetwork.hosts()))))
