from netmiko import ConnectHandler

device={
    'device_type': 'cisco_ios_telnet',
    'ip': '10.1.102.160',
    'username': 'admin',
    'password': 'cisco',
    'secret': 'cisco',

}

net_connect = None

try:
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    print("Telnet login successful!")
except Exception as e:
    print(f"Telnet login failed_ {str(e)}")

finally:
    try:
        if net_connect:
            net_connect.disconnect()
            print("Disconnected from the device")
    except NameError:
        pass