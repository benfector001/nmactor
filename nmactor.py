import subprocess
import os
import time
import re
import sys

# Tenta importar o Colorama
try:
    from colorama import init, Fore, Style
except ImportError:
    print("Colorama não encontrado! Instalando agora...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import init, Fore, Style

# Inicializa o Colorama
init(autoreset=True)

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def mostrar_desenho():
    pinguim = [
        f"       {Fore.YELLOW}{Style.BRIGHT}.--.",
        f"      {Fore.CYAN}|o_o |",
        f"      {Fore.RED}|:_/ |",
        f"     {Fore.GREEN}//   \\ \\",
        f"    {Fore.MAGENTA}(|     | )",
        f"   {Fore.BLUE}/'\\_   _/`\\",
        f"   {Fore.YELLOW}\\___)=(___/"
    ]

    for linha in pinguim:
        print(linha)
        time.sleep(0.3)
    time.sleep(1)

def exibir_mensagens():
    print(f"\n{Fore.GREEN}Feito por by Benfector001")
    print(f"{Fore.GREEN}Este é um software simples de verificação usando Nmap.")
    print(f"{Fore.YELLOW}Certifique-se de ter o Nmap instalado!\n")
    time.sleep(1)

def verificar_nmap_instalado():
    try:
        subprocess.run(['nmap', '--version'], check=True, capture_output=True, text=True)
    except FileNotFoundError:
        print(f"\n{Fore.RED}Erro: O Nmap não está instalado no sistema.")
        exit()

def validar_ip(ip):
    padrao_ip = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if padrao_ip.match(ip):
        octetos = ip.split(".")
        for octeto in octetos:
            if not (0 <= int(octeto) <= 255):
                return False
        return True
    return False

def varredura_simples(ip):
    print(f"\n{Fore.YELLOW}Executando varredura simples...")
    result = subprocess.run(['nmap', ip], capture_output=True, text=True)
    print(result.stdout)

def varredura_com_portas(ip, portas):
    print(f"{Fore.YELLOW}Executando varredura nas portas {portas}...")
    result = subprocess.run(['nmap', '-p', portas, ip], capture_output=True, text=True)
    print(result.stdout)

def varredura_com_deteccao_de_versao(ip):
    print(f"\n{Fore.YELLOW}Executando varredura com detecção de versão...")
    result = subprocess.run(['nmap', '-sV', ip], capture_output=True, text=True)
    print(result.stdout)

def varredura_vulnerabilidades(ip):
    print(f"\n{Fore.YELLOW}Executando varredura de vulnerabilidades...")
    result = subprocess.run(['nmap', '--script', 'vuln', ip], capture_output=True, text=True)
    print(result.stdout)

def salvar_relatorio(result, ip, tipo_varredura):
    nome_arquivo = f"relatorio_{tipo_varredura}_{ip}.txt"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(result.stdout)
    print(f"\n{Fore.GREEN}Relatório salvo em: {os.path.abspath(nome_arquivo)}")

def menu_avancado(ip):
    print(f"\n{Fore.CYAN}=== Sub-menu de Verificação Avançada ===")
    print(f"{Fore.MAGENTA}1 - Usar nmap com -v (verbose) e -T4 (tempo otimizado)")
    print(f"{Fore.YELLOW}2 - Usar nmap com portas específicas")
    print(f"{Fore.RED}3 - Usar nmap com detecção de versão (-sV)")
    print(f"{Fore.BLUE}4 - Usar nmap para vulnerabilidades (scripts)")
    print(f"{Fore.GREEN}5 - Voltar ao menu principal")
    
    escolha = input(f"\n{Fore.CYAN}Escolha uma opção (1, 2, 3, 4 ou 5): ")
    
    if escolha == '1':
        result = subprocess.run(['nmap', '-v', '-T4', ip], capture_output=True, text=True)
        print(result.stdout)
        salvar = input(f"\n{Fore.YELLOW}Deseja salvar este relatório? (s/n): ").lower()
        if salvar == 's':
            salvar_relatorio(result, ip, "avancada")
    elif escolha == '2':
        portas = input(f"\n{Fore.YELLOW}Digite as portas que deseja verificar (ex: 22,80,443): ")
        varredura_com_portas(ip, portas)
    elif escolha == '3':
        varredura_com_deteccao_de_versao(ip)
    elif escolha == '4':
        varredura_vulnerabilidades(ip)
    elif escolha == '5':
        return
    else:
        print(f"{Fore.RED}Opção inválida! Por favor, escolha 1, 2, 3, 4 ou 5.")
        menu_avancado(ip)

def exibir_menu():
    print(f"\n{Fore.CYAN}=== Menu de Seleção ===")
    print(f"{Fore.YELLOW}1 - Verificação simples (nmap básico)")
    print(f"{Fore.RED}2 - Verificação avançada (nmap com opções avançadas)")
    print(f"{Fore.GREEN}3 - Verificação de vulnerabilidades (nmap --script=vuln)")
    print(f"{Fore.MAGENTA}4 - Sair")
    
    escolha = input(f"{Fore.CYAN}Escolha uma opção (1, 2, 3 ou 4): ")
    return escolha

def main():
    exibir_mensagens()
    mostrar_desenho()
    verificar_nmap_instalado()

    print()
    ip = input(f"{Fore.GREEN}Digite o IP para a varredura: ")
    while not validar_ip(ip):
        print(f"\n{Fore.RED}Erro: O IP inserido é inválido. Por favor, insira um IP válido.")
        ip = input(f"{Fore.GREEN}Digite o IP para a varredura: ")

    while True:
        escolha = exibir_menu()

        if escolha == '1':
            varredura_simples(ip)
        elif escolha == '2':
            menu_avancado(ip)
        elif escolha == '3':
            varredura_vulnerabilidades(ip)
        elif escolha == '4':
            print(f"\n{Fore.GREEN}Saindo...")
            break
        else:
            print(f"{Fore.RED}Opção inválida! Por favor, escolha 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()
