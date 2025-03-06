import os
import subprocess
import platform
import sys
import ctypes
import time

# Detectar se o terminal suporta cores ANSI (evitar caracteres estranhos no CMD padrão do Windows)
SUPORTE_ANSI = sys.stdout.isatty() and os.name != "nt"

# Definir as cores apenas se ANSI for suportado
RESET = "\033[0m" if SUPORTE_ANSI else ""
GREEN = "\033[92m" if SUPORTE_ANSI else ""
YELLOW = "\033[93m" if SUPORTE_ANSI else ""
BLUE = "\033[94m" if SUPORTE_ANSI else ""
RED = "\033[91m" if SUPORTE_ANSI else ""

# Lista de servidores KMS públicos
KMS_SERVERS = [
    "kms8.msguides.com",
    "kms.digiboy.ir",
    "kms.lotro.cc",
    "kms.cangshui.net"
]

# Dicionário de chaves KMS genéricas atualizado
KMS_KEYS = {
    "Microsoft Windows 11 Pro": "W269N-WFGWX-YVC9B-4J6C9-T83GX",
    "Microsoft Windows 11 Home": "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
    "Microsoft Windows 10 Pro": "W269N-WFGWX-YVC9B-4J6C9-T83GX",
    "Microsoft Windows 10 Home": "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99",
    "Microsoft Windows 10 Education": "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2",
    "Microsoft Windows 10 Enterprise": "NPPR9-FWDCX-D2C8J-H872K-2YT43",
    "Microsoft Windows 8.1 Pro": "GCRJD-8NW9H-F2CDX-CCM8D-9D6T9",
    "Microsoft Windows 8.1 Enterprise": "MHF9N-XY6XB-WVXMC-BTDCT-MKKG7",
    "Microsoft Windows 8 Pro": "NG4HW-VH26C-733KW-K6F98-J8CK4",
    "Microsoft Windows 8 Enterprise": "32JNW-9KQ84-P47T8-D8GGY-CWCK7",
    "Microsoft Windows 7 Professional": "FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4",
    "Microsoft Windows 7 Enterprise": "33PXH-7Y6KF-2VJC9-XBBR8-HVTHH"
}

def run_as_admin():
    """Reinicia o script com permissões de administrador, se necessário."""
    if ctypes.windll.shell32.IsUserAnAdmin():
        return  
    print(f"{YELLOW}[INFO] Reexecutando como administrador...{RESET}")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

run_as_admin()

def get_windows_version():
    """Detecta a versão exata do Windows de forma compatível com Windows 10 e 11."""
    try:
        result = subprocess.check_output(
            ["powershell", "-Command", "(Get-CimInstance Win32_OperatingSystem).Caption"],
            universal_newlines=True
        ).strip()

        if result in KMS_KEYS:
            return result

        print(f"{RED}[ERRO] Versão do Windows não encontrada no banco de chaves: {result}{RESET}")
        return None
    except Exception as e:
        print(f"{RED}[ERRO] Falha ao detectar a versão do Windows! {e}{RESET}")
        return None

def activate_windows():
    """Ativa o Windows via KMS usando servidores públicos"""
    edition = get_windows_version()
    if not edition:
        print(f"{RED}[ERRO] Não foi possível detectar a versão do Windows.{RESET}")
        return

    kms_key = KMS_KEYS.get(edition, None)
    if not kms_key:
        print(f"{RED}[ERRO] Versão do Windows não suportada para ativação via KMS: {edition}{RESET}")
        return

    print(f"{YELLOW}[INFO] Aplicando chave KMS para {edition}...{RESET}")
    os.system(f"slmgr /ipk {kms_key}")

    for server in KMS_SERVERS:
        print(f"{YELLOW}[INFO] Tentando ativação no servidor: {server}{RESET}")
        os.system(f"slmgr /skms {server}")
        time.sleep(2)
        result = os.system("slmgr /ato")
        time.sleep(2)

        if result == 0:  # Se ativou com sucesso, para aqui
            print(f"{GREEN}[SUCESSO] {edition} ativado com sucesso usando {server}!{RESET}")
            return  

    print(f"{RED}[ERRO] Nenhum servidor KMS conseguiu ativar o Windows.{RESET}")

def activate_office():
    """Ativa o Microsoft Office via KMS usando servidores públicos"""
    print(f"{YELLOW}[INFO] Aplicando chave KMS...{RESET}")
    os.system(r'cscript //nologo "C:\Program Files\Microsoft Office\Office16\OSPP.VBS" /inpkey:XXXXX-XXXXX-XXXXX-XXXXX-XXXXX')

    for server in KMS_SERVERS:
        print(f"{YELLOW}[INFO] Tentando ativação do Office no servidor: {server}{RESET}")
        os.system(rf'cscript //nologo "C:\Program Files\Microsoft Office\Office16\OSPP.VBS" /sethst:{server}')
        time.sleep(2)
        result = os.system(r'cscript //nologo "C:\Program Files\Microsoft Office\Office16\OSPP.VBS" /act')
        time.sleep(2)

        if result == 0:  # Se ativou com sucesso, para aqui
            print(f"{GREEN}[SUCESSO] Office ativado com sucesso usando {server}!{RESET}")
            return  

    print(f"{RED}[ERRO] Nenhum servidor KMS conseguiu ativar o Office.{RESET}")

def remove_windows_license():
    """Remove a licença atual do Windows e limpa o histórico de chaves"""
    print(f"{YELLOW}[INFO] Removendo licença do Windows...{RESET}")
    os.system("slmgr /upk")  # Remove a chave de produto instalada
    os.system("slmgr /cpky")  # Remove a chave do registro
    os.system("slmgr /rearm")  # Reseta o status da ativação
    os.system("net stop sppsvc && net start sppsvc")  # Reinicia o serviço de licenciamento

    print(f"{GREEN}[SUCESSO] Licença removida e histórico limpo!{RESET}")

def menu():
    """Exibe o menu e permite múltiplas execuções"""
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela

        print("=" * 40)
        print("🔥 Z3R0 ACTIVATOR 🔥".center(40))
        print("=" * 40)

        print("\n[MENU] Escolha uma opção:")
        print("1️ - Ativar Windows")
        print("2️ - Ativar Office")
        print("3️- Ativar Ambos")
        print("4️ - Remover Licença Atual")
        print("5️ - Sair\n")

        opcao = input("Digite sua escolha (1, 2, 3, 4 ou 5): ")

        if opcao == "1":
            activate_windows()
        elif opcao == "2":
            activate_office()
        elif opcao == "3":
            activate_windows()
            activate_office()
        elif opcao == "4":
            remove_windows_license()
        elif opcao == "5":
            print("[INFO] Encerrando programa...")
            time.sleep(2)
            print("[INFO] Programa encerrado!")
            print("[INFO] Obrigado por usar o Z3R0 ACTIVATOR!")
            time.sleep(2)
            sys.exit()
        else:
            print(f"{RED}[ERRO] Opção inválida!{RESET}")
        time.sleep(2)

menu()
