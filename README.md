# 🛠️ Scripts y Explotaciones de Ciberseguridad Ofensiva

¡Bienvenido a mi laboratorio de aprendizaje de hacking ético!  
Este repositorio documenta mi progreso paso a paso mientras aprendo y practico técnicas reales de Red Team contra máquinas vulnerables como **Metasploitable 2**.  
Cada carpeta contiene una explotación o herramienta desarrollada por mí, con sus respectivos scripts, capturas y writeups detallados en Markdown.

---

## 🧠 Objetivos del repositorio

- Aprender técnicas reales de hacking ético ⚔️  
- Automatizar tareas con Python 🐍  
- Entender vulnerabilidades clásicas y cómo se explotan 🔥  
- Practicar con máquinas como Metasploitable 2 🧪  
- Documentar todo con claridad, capturas y análisis 📚

---

## 📁 Índice de Explotaciones

| Explotación | Servicio | CVE / Técnica | Link |
|------------|----------|----------------|------|
| 🔓 vsftpd 2.3.4 Backdoor | FTP | [CVE-2011-2523](https://nvd.nist.gov/vuln/detail/CVE-2011-2523) | [Ver Writeup](./exploits/vsftpd-234-backdoor/README.md) |
| 📂 Samba 3.0.20 - Usermap Script | SMB | [CVE-2007-2447](https://nvd.nist.gov/vuln/detail/CVE-2007-2447) | [Ver Writeup](./exploits/samba-usermap-cve2007-2447/README.md) |

---

## 🧪 Herramientas y Scripts Propios

| Script | Descripción | Link |
|--------|-------------|------|
| 🔍 Escáner de Puertos | Escaneo simple con sockets en Python | [Ver script](./scripts/port_scanner.py) |
| 🎯 Banner Grabbing | Obtener banners de servicios abiertos | [Ver script](./scripts/banner_grabber.py) |
| 🌐 Subdomain Enumerator | Enumeración de subdominios via wordlist | [Ver script](./scripts/subdomain_enum.py) |
| 💣 Fuerza Bruta Login | Ataque por diccionario a formularios login | [Ver script](./scripts/bruteforce_login.py) |
| 🛰️ Escaneo con Nmap Automático | Script que lanza Nmap y guarda resultados | [Ver script](./scripts/nmap_scan.py) |

---

## 📸 Capturas de las prácticas

Cada explotación contiene una carpeta `evidencias/` con imágenes relevantes:



---

## 🚧 En progreso

- 📦 Organización del repositorio
- 🛠️ Automatización con Bash y Python
- 🧠 Preparación para plataformas: TryHackMe, HackTheBox, Dockerlabs...

---

## 🧭 Próximos pasos

➡️ Finalizar las explotaciones manuales sin Metasploit  
➡️ Empezar con máquinas de **TryHackMe** y **HackTheBox**  
➡️ Subir soluciones paso a paso para cada máquina  
➡️ Crear herramientas personalizadas para facilitar el proceso

---

## 📬 Contacto

Si tienes sugerencias o quieres colaborar, puedes encontrarme en:

- GitHub: [@doval2222](https://github.com/doval2222)
- LinkedIn: *(enlaza aquí tu perfil si quieres)*

---

> 📌 **Disclaimer:** Este repositorio es únicamente con fines educativos. Todo se realiza en entornos controlados y legales. No me hago responsable del uso indebido de esta información.
