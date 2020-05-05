import paramiko 
import time


HOST = "10.10.20.70" 
user_name = 'admin'
time.sleep(1)
pass_word = 'admin'
time.sleep(1)
# f = open('mangerIP')

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=HOST, username=user_name, password=pass_word)

remote_connection = ssh_client.invoke_shell()

remote_connection.send('config t' + '\n')
time.sleep(1)
remote_connection.send('vpn 512' + '\n')
time.sleep(1)
remote_connection.send('int eth1' + '\n')
time.sleep(1)
remote_connection.send('no shut' + '\n')
time.sleep(1)
remote_connection.send('ip add 4.4.4.4/24' + '\n')
time.sleep(1)
remote_connection.send('end' + '\n')
time.sleep(1)
remote_connection.send('yes' + '\n')
time.sleep(2)

# for IP in f:
# 	IP=IP.strip() 
#     print ("IP for switch:" + (IP))
#     HOST = IP

#     remote_connection.send("config..." + str(i) + "\n")
#     time.sleep(0.5)


# time.sleep(1)
#output = remote_connection.recv(65535)
#print output

ssh_client.close()
