# Escáner Nmap Personal ⚙️

Este script realiza un escaneo básico pero informativo sobre un objetivo con Nmap, guardando la salida en un archivo organizado.

---

## 🛠️ Uso

```bash
python3 nmap_scan.py

Se te pedirá la IP de la víctima:

Introduce la IP del objetivo (ej: 192.168.1.10)


El resultado se guarda automáticamente como:

192.168.1.10_scan.txt

🔍 Escaneo realizado con:
-sV: Versión de servicios

-sC: Scripts NSE por defecto

-Pn: No hace ping previo

-oN: Guarda salida normal en archivo