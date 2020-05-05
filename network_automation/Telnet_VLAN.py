
import getpass
import telnetlib 

HOST = "10.10.20.60"
user = 'admin'
password = 'admin'

# f = open('managerip')


tn = telnetlib.Telnet(HOST)


tn.write(b"conf t\n")
tn.write(b"vpn 512\n")

for n in range (1,3):
    tn.write(b"int eth" + str(n).encode("ascii") + b"\n")  
    tn.write(b"no sh\n")
    tn.write(b"192.168.1." + str(n).encode("ascii")+ b"/24" + b"\n")

tn.write(b"end\n")
tn.write(b"yes\n")
tn.write(b"exit\n")

print(tn.read_all())




# for IP in f:
#     IP=IP.strip() 
#     print ("IP for switch:" + (IP))
#     HOST = IP
#     tn = telnetlib.Telnet(HOST)
#     tn.read_until(b"Username: ")
#     tn.write(user.encode('ascii') + b"\n")
#     if password:
#         tn.read_until(b"Password: ")
#         tn.write(password.encode('ascii') + b"\n")
   
#     tn.write(b"conf t\n")
#     tn.write(b"vpn 512\n")
    
#     for n in range (1,3):
#         tn.write(b"int eth" + str(n).encode("ascii") + b"\n")  
#         tn.write(b"no sh\n")
#         tn.write(b"192.168.1." + str(n).encode("ascii")+ b"/24" + b"\n")

#     tn.write(b"end\n")
#     tn.write(b"yes\n")
#     tn.write(b"exit\n")
    
#     print(tn.read_all().decode('ascii'))

