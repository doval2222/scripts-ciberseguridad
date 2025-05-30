# Subdomain Enumerator 🕵️‍♂️

Este script realiza una **enumeración de subdominios** sobre un dominio objetivo, utilizando una lista de nombres comunes.

Es una técnica típica en la fase de reconocimiento durante un pentest web, útil para descubrir subdominios ocultos o mal configurados que podrían revelar servicios expuestos.

---

## 🚀 Uso

```bash
python3 subdomain_enum.py

Introduce el dominio objetivo (sin http/https): ejemplo.com

✅ Ejemplo de salida

[+] Encontrado: admin.ejemplo.com -> 192.168.1.5
[+] Encontrado: vpn.ejemplo.com -> 192.168.1.8