import socket

def subdomain_enum(domain, wordlist):
    with open(wordlist, "r") as f:
        subdomains = f.read().splitlines()

    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(subdomain)
            print(f"[+] Encontrado: {subdomain} -> {ip}")
        except socket.gaierror:
            pass

if __name__ == "__main__":
    objetivo = input("Introduce el dominio objetivo (sin http/https): ")
    wordlist = "subdomains.txt"
    subdomain_enum(objetivo, wordlist)
