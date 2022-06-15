from netmiko import ConnectHandler
import paramiko
import netmiko
import sys
from getpass import getpass

CSR = {
    'device_type': 'cisco_ios',
    'ip': input('Enter ip address: '),
    'username': 'marsad',
    'password': 'cisco'
}

net_connect = ConnectHandler(**CSR)
hostname = net_connect.send_command('show run | i host')
hostname.split(" ")
hostname,device = hostname.split(" ")
print ("Backing up " + device)

filename = '/home/marsad/backups/' + device + '.txt'

showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")

net_connect.disconnect()

