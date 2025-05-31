import os

def run_nmap_scan(target):
    output_file = f"{target}_scan"
    print(f"[+] Escaneando {target}...")

    os.system(f"nmap -sV -sC -Pn -oN {output_file}.txt {target}")
    print(f"[+] Escaneo guardado en {output_file}.txt")

if __name__ == "__main__":
    objetivo = input("Introduce la IP del objetivo (ej: 192.168.1.10): ")
    run_nmap_scan(objetivo)
