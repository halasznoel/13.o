import paramiko
import time

def cisco_login(hostname, username, password, enable_password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(hostname, username=username, password=password, allow_agent=False, look_for_keys=False)
        channel = ssh.invoke_shell()
        time.sleep(1)
        output = channel.recv(65535).decode('utf-8')
        print(output)
        if '#' in output or '>' in output:
            channel.send("enable\n")
            time.sleep(1)
            channel.send(enable_password+"\n")
            time.sleep(1)
            enable_output = channel.recv(65535).decode('utf-8')
            print(enable_output)
            if '#' in enable_output:
                print('Login successful! Entered privilege mode')
            else:
                print("Enable mode failed!")
                print("Login failed")
        else:
            print("Login failed")
        if '#' in enable_output:
            print("Login successful! Entered privilege mode")
            channel.send("show ip interface brief\n")
            time.sleep(2)
            channel.send(" ")
            time.sleep(1)
            ip_int_brief_output = channel.recv(65535).decode('utf-8')
            print(ip_int_brief_output)
        else:
            print("Enable mode failed")
            print("Login failed")
        ssh.close()
    except Exception as e:
        print(f"Error: {e}")
        print("Login failed!")
if __name__ == "__main__":
    device_hostname = "10.1.102.160"
    device_username = "admin"
    device_password = "cisco"
    device_enable_password = "cisco"


cisco_login(device_hostname, device_username, device_password,device_enable_password)