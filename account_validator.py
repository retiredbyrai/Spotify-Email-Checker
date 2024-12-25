import os
import time
import requests
from colorama import Fore, Style

# Variables globales
USERS_SOURCE_PATH = ''
PROXIES = []
USE_PROXIES = False
MAX_THREADS = 10
RESULTS_DIR = 'results'
RESULTS_FILE_NAME = f'{RESULTS_DIR}/results-{time.strftime("%Y-%m-%d_%H-%M-%S")}.txt'
PROXY_TYPE = 'HTTP'  # Proxy por defecto

# Funciones para mostrar el menú
def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar terminal
    print(Fore.GREEN + "\nSpotify Email Checker\n" + Style.RESET_ALL)
    print(Fore.YELLOW + f"1. Importar Cuentas [Cuentas Importadas: {USERS_SOURCE_PATH if USERS_SOURCE_PATH else 'No importadas'}]" + Style.RESET_ALL)
    print(Fore.YELLOW + f"2. Validar Cuentas [Preparado para Validar]" + Style.RESET_ALL)
    print(Fore.YELLOW + f"3. Activar Proxies [Proxies {'Habilitadas' if USE_PROXIES else 'Deshabilitadas'}]" + Style.RESET_ALL)
    print(Fore.YELLOW + f"4. Configurar Número de Hilos [Número de Hilos: {MAX_THREADS}]" + Style.RESET_ALL)
    print(Fore.YELLOW + f"5. Importar Proxies [Proxies {'Importadas' if PROXIES else 'No importadas'}]" + Style.RESET_ALL)
    print(Fore.YELLOW + f"6. Elegir Tipo de Proxy [Tipo de Proxy: {PROXY_TYPE}]" + Style.RESET_ALL)
    print(Fore.YELLOW + "7. Salir" + Style.RESET_ALL)

def import_accounts():
    global USERS_SOURCE_PATH
    USERS_SOURCE_PATH = input("Introduce la ruta del archivo de cuentas: ")
    print(Fore.CYAN + f"Cuentas importadas de: {USERS_SOURCE_PATH}" + Style.RESET_ALL)
    time.sleep(1)

def load_accounts(file_path):
    """Carga las cuentas desde el archivo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(Fore.RED + f"Archivo '{file_path}' no encontrado." + Style.RESET_ALL)
        return []

def check_email_exists(email):
    """Verifica si el correo existe en Spotify"""
    url = "https://spclient.wg.spotify.com/signup/public/v1/account?validate=1"
    payload = {'email': email}
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            data = response.json()
            if "errors" in data and "email" in data["errors"]:
                if data["errors"]["email"] == "That email is already registered to an account.":
                    return True  # Email existe
        return False  # Email no existe
    except requests.RequestException as e:
        print(Fore.RED + f"[ERROR] Error al verificar {email}: {str(e)}" + Style.RESET_ALL)
        return False

def validate_accounts():
    if not USERS_SOURCE_PATH:
        print(Fore.RED + "Primero importa un archivo de cuentas." + Style.RESET_ALL)
        return

    accounts = load_accounts(USERS_SOURCE_PATH)
    if not accounts:
        print(Fore.RED + "No hay cuentas para validar. Importa un archivo válido." + Style.RESET_ALL)
        return

    print(Fore.CYAN + "Iniciando validación..." + Style.RESET_ALL)
    for account in accounts:
        email, password = account.split(":")
        if check_email_exists(email):
            print(Fore.GREEN + f"Cuenta válida: {email}" + Style.RESET_ALL)
            with open(RESULTS_FILE_NAME, 'a', encoding='utf-8') as file:
                file.write(f"{email}:{password}\n")
        else:
            print(Fore.RED + f"Cuenta no encontrada: {email}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Validación completa. Resultados guardados en '{RESULTS_FILE_NAME}'." + Style.RESET_ALL)

def toggle_proxies():
    global USE_PROXIES
    USE_PROXIES = not USE_PROXIES
    if USE_PROXIES:
        print(Fore.GREEN + "Proxies habilitadas." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Proxies deshabilitadas." + Style.RESET_ALL)
    time.sleep(1)

def import_proxies():
    proxy_file = input("Introduce la ruta del archivo de proxies: ")
    if os.path.exists(proxy_file):
        global PROXIES
        with open(proxy_file, 'r', encoding='utf-8') as file:
            PROXIES = [line.strip() for line in file if line.strip()]
        print(Fore.CYAN + f"Proxies importadas de: {proxy_file}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Archivo '{proxy_file}' no encontrado." + Style.RESET_ALL)
    time.sleep(1)

def configure_threads():
    global MAX_THREADS
    threads = input(f"Introduce el número de hilos (actual: {MAX_THREADS}): ")
    if threads.isdigit():
        MAX_THREADS = int(threads)
        print(Fore.CYAN + f"El número de hilos ha sido configurado a: {MAX_THREADS}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Valor no válido. Debes ingresar un número." + Style.RESET_ALL)
    time.sleep(1)

def choose_proxy_type():
    global PROXY_TYPE
    print(Fore.CYAN + "Elige el tipo de proxy:" + Style.RESET_ALL)
    print("1. HTTP")
    print("2. HTTPS")
    print("3. SOCKS4")
    print("4. SOCKS5")
    choice = input("Selecciona un tipo de proxy (1-4): ")
    
    if choice == '1':
        PROXY_TYPE = 'HTTP'
    elif choice == '2':
        PROXY_TYPE = 'HTTPS'
    elif choice == '3':
        PROXY_TYPE = 'SOCKS4'
    elif choice == '4':
        PROXY_TYPE = 'SOCKS5'
    else:
        print(Fore.RED + "Selección no válida. El tipo de proxy no ha cambiado." + Style.RESET_ALL)
        return
    
    print(Fore.CYAN + f"Tipo de proxy configurado a: {PROXY_TYPE}" + Style.RESET_ALL)
    time.sleep(1)

def main():
    while True:
        print_menu()
        choice = input("Selecciona una opción: ")

        if choice == '1':
            import_accounts()
        elif choice == '2':
            validate_accounts()
        elif choice == '3':
            toggle_proxies()
        elif choice == '4':
            configure_threads()
        elif choice == '5':
            import_proxies()
        elif choice == '6':
            choose_proxy_type()
        elif choice == '7':
            print(Fore.YELLOW + "Saliendo..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción no válida. Inténtalo de nuevo." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
