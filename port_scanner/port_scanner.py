import socket

ip = input("IP objetivo:")
for port in range(20, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"[+] Puerto abierto: {port}")
    s.close()