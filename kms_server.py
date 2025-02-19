import os
import subprocess
import threading
import time
from flask import Flask, request

RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"

app = Flask(__name__)

KMS_RESPONSE = {
    "status": "success",
    "message": "Windows ativado com sucesso!",
    "license_key": "W269N-WFGWX-YVC9B-4J6C9-T83GX"
}

@app.route('/kms', methods=['POST'])
def kms_activation():
    """Simula uma resposta do servidor KMS"""
    data = request.json
    if data.get("request") == "activation":
        return KMS_RESPONSE
    else:
        return {"status": "error", "message": "Requisição inválida"}

def start_kms_server():
    """Executa o servidor KMS em uma thread separada"""
    print(f"{BLUE}[INFO] Iniciando servidor KMS na porta 1688...{RESET}")
    time.sleep(2)
    app.run(host="0.0.0.0", port=1688, debug=False)

def activate_windows():
    """Executa os comandos de ativação no Windows"""
    print(f"{YELLOW}[INFO] Configurando o servidor KMS no Windows...{RESET}")
    os.system("slmgr /skms 127.0.0.1")
    
    print(f"{YELLOW}[INFO] Solicitando ativação...{RESET}")
    os.system("slmgr /ato")
    
    print(f"{GREEN}[SUCESSO] Ativação concluída com sucesso!{RESET}")

if __name__ == '__main__':
    print(f"{BLUE}======================================={RESET}")
    print(f"{GREEN}        🔥 ZERO ACTIVATOR 🔥{RESET}")
    print(f"{BLUE}=======================================\n{RESET}")
    
    threading.Thread(target=start_kms_server, daemon=True).start()

    time.sleep(3)

    activate_windows()

    print(f"\n{GREEN}✅ Processo concluído! Feche esta janela ou pressione ENTER para sair.{RESET}")
    input()
