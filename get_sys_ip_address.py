import socket

host_name=socket.gethostname()
ip=socket.gethostbyname(host_name)

print(f"your system name is :{host_name} and ip address is : {ip}")