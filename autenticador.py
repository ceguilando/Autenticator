from pyperclip import copy
import sys
import pyotp
import time

def main():
    if len(sys.argv) != 2:
        print("Uso: autenticador.py \"CLAVE_SECRETA_BASE32\"")
        sys.exit(1)

    secret = sys.argv[1].strip()

    try:
        totp = pyotp.TOTP(secret)
    except Exception as e:
        print(f"Error creando TOTP: {e}")
        sys.exit(1)

    code = totp.now()
    # segundos restantes del intervalo actual (30s por defecto)
    remaining = 30 - int(time.time()) % 30

    print(code)
    copy(code)
if __name__ == "__main__":
    main()