# nmactor
### Verificador de IP com Nmap

Este é um software simples de verificação de IP, utilizando a ferramenta Nmap para realizar varreduras de segurança e detecção de vulnerabilidades. O programa permite que você execute varreduras básicas e avançadas em qualquer endereço IP, verificando portas abertas, serviços e até mesmo vulnerabilidades conhecidas.

### Funcionalidades:
- **Verificação Simples**: Realiza uma varredura básica no IP fornecido.
- **Verificação Avançada**: Permite a escolha de diferentes opções de varredura, como detecção de versão e verificação de portas específicas.
- **Verificação de Vulnerabilidades**: Executa uma verificação de vulnerabilidades utilizando os scripts do Nmap.
- **Relatório de Resultados**: Os resultados das varreduras podem ser salvos em arquivos de texto para análise posterior.

### Como Usar:

1. **Instalar o Nmap**:
   - Certifique-se de que o Nmap está instalado no seu sistema. Caso contrário, instale-o conforme a documentação oficial:
     - [Instalação do Nmap](https://nmap.org/book/install.html)

2. **Baixar o Projeto**:
   - Clone este repositório usando o Git:
     ```bash
     git clone https://github.com/benfector001/nmactor.git
     ```

3. **Acessar o Diretório**:
   - Navegue até o diretório do projeto:
     ```bash
     cd nmactor
     ```

4. **Executar o Programa**:
   - Execute o arquivo Python:
     ```bash
     python nmactor.py
     ```

5. **Escolha a Opção de Verificação**:
   - Você será solicitado a inserir um endereço IP para a varredura.
   - Escolha uma das opções de varredura (simples, avançada, vulnerabilidades).

### Requisitos:
- Python 3.x
- Nmap instalado no sistema
