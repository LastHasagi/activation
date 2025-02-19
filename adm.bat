@echo off
:: Verifica se está rodando como administrador
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Solicitando privilégios administrativos...
    powershell Start-Process kms_server.exe -Verb runAs
    exit
)
:: Executa o EXE normalmente
kms_server.exe
