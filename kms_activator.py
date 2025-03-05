import os
import threading
import time
import random
import string
from flask import Flask, request
import logging
import sys

RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app.logger.setLevel(logging.ERROR)

def generate_license_key():
    """Gera uma chave de licença no formato XXXXX-XXXXX-XXXXX-XXXXX-XXXXX"""
    segments = []
    for _ in range(5):
        segment = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        segments.append(segment)
    return '-'.join(segments)

@app.route('/kms', methods=['POST'])
def kms_activation():
    """Simula uma resposta do servidor KMS"""
    data = request.json
    if data.get("request") == "activation":
        KMS_RESPONSE = {
            "status": "success",
            "message": "Ativação concluída com sucesso!",
            "license_key": generate_license_key()
        }
        return KMS_RESPONSE
    else:
        return {"status": "error", "message": "Requisição inválida"}

def start_kms_server():
    """Executa o servidor KMS em uma thread separada"""
    print(f"{BLUE}[INFO] Iniciando conexão ao Servidor...{RESET}")
    time.sleep(2)

    app.run(host="0.0.0.0", port=1688, debug=False, use_reloader=False)

def activate_windows():
    """Ativação do Windows via KMS"""
    print(f"{YELLOW}[INFO] Conectando ao servidor Z3R0-Windows-activator...{RESET}")
    os.system("slmgr /skms 127.0.0.1")

    print(f"{YELLOW}[INFO] Solicitando Activation-Key...{RESET}")
    os.system("slmgr /ato")

    print(f"{GREEN}[SUCESSO] Windows ativado com sucesso!{RESET}")

def remove_windows_license():
    """Remove a licença atual do Windows"""
    print(f"{RED}[INFO] Removendo licença atual do Windows...{RESET}")
    os.system("slmgr /upk")
    os.system("slmgr /cpky")
    print(f"{GREEN}[SUCESSO] Licença removida!{RESET}")

def activate_office():
    """Ativação do Office via KMS"""
    print(f"{YELLOW}[INFO] Conectando ao servidor Z3R0-Office-activator...{RESET}")
    os.system('cscript //nologo "C:\\Program Files\\Microsoft Office\\Office16\\OSPP.VBS" /sethst:127.0.0.1')
    
    print(f"{YELLOW}[INFO] Aplicando chave KMS para o Office...{RESET}")
    os.system('cscript //nologo "C:\\Program Files\\Microsoft Office\\Office16\\OSPP.VBS" /inpkey:XXXXX-XXXXX-XXXXX-XXXXX-XXXXX')

    print(f"{YELLOW}[INFO] Solicitando ativação do Office...{RESET}")
    os.system('cscript //nologo "C:\\Program Files\\Microsoft Office\\Office16\\OSPP.VBS" /act')

    print(f"{GREEN}[SUCESSO] Microsoft Office ativado com sucesso!{RESET}")

if __name__ == '__main__':
    print(f"{BLUE}======================================={RESET}")
    print(f"{GREEN}        🔥 Z3R0 ACTIVATOR 🔥{RESET}")
    print(f"{BLUE}=======================================\n{RESET}")

    threading.Thread(target=start_kms_server, daemon=True).start()

    time.sleep(0.5)
    
    print(f"{GREEN}        STARTING SERVER... {RESET}")
    
    time.sleep(1.5)
    
    print(f"{BLUE}=======================================\n{RESET}")
    print(f"{YELLOW}[INFO] Conexão bem sucedida! {RESET}")
    time.sleep(0.2)
    print(f"{YELLOW}[INFO] Host encontrado!{RESET}\n")
    print(f"{YELLOW}[INFO] Aguardando solicitações de ativação...{RESET}\n")

    print(f"{YELLOW}[MENU] Escolha uma opção:{RESET}")
    print(f"1️⃣ - Ativar Windows")
    print(f"2️⃣ - Ativar Office")
    print(f"3️⃣ - Ativar Ambos")
    print(f"4️⃣ - Remover Licença Atual do Windows\n")

    opcao = input(f"{BLUE}Digite sua escolha (1, 2, 3 ou 4): {RESET}")

    if opcao == "1":
        activate_windows()
    elif opcao == "2":
        activate_office()
    elif opcao == "3":
        activate_windows()
        activate_office()
    elif opcao == "4":
        remove_windows_license()
    else:
        print(f"{RED}[ERRO] Opção inválida!{RESET}")

    print(f"\n{GREEN}✅ Processo concluído! Pressione ENTER para sair.{RESET}")
    input()