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
        for host_number in range(220,250):
            channel.send("ping ip 10.1.1.%s size 36 repeat 1 timeout 1" % host_number + "\n")
            time.sleep(2)
            ping_output = channel.recv(65535).decode('utf-8')
            successful = ping_output.count("Success rate is 100 percent")
            if successful > 0:
                print(ping_output)
            else:
                print("10.1.1.%s is not on-like" % host_number)
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