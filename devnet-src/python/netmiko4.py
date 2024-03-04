from netmiko import ConnectHandler

iosv_R1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.252',
    'username': 'cisco',
    'password': 'cisco123!',
}

iosv_R2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.130',
    'username': 'cisco',
    'password': 'cisco123!',
}

iosv_R3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.191',
    'username': 'cisco',
    'password': 'cisco123!',
}


with open('Base_Config') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [iosv_R1, iosv_R2, iosv_R3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)


with open('Base2_Config') as f:
    lines = f.read().splitlines()
print (lines)


all_devices1 = [iosv_R1, iosv_R2]

for devices in all_devices1:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)