import socket

def banner_grab(ip, port):
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((ip, port))
        # Enviar una solicitud HTTP si el puerto es 80
        if port == 80:
            s.sendall(b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
        banner = s.recv(2048).decode(errors="ignore")
        print(f"[+] Banner de {ip}:{port}:\n")
        print(banner)
        s.close()
    except Exception as e:
        print(f"[-] No se pudo obtener banner de {ip}:{port}")
        print(f"Error: {e}")

if __name__ == "__main__":
    objetivo = input("Introduce la IP o dominio a escanear: ")
    puerto = int(input("Introduce el puerto (por ejemplo 80 o 21): "))
    banner_grab(objetivo, puerto)
 