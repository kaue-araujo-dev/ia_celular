# 📱 Terminal Device Controller (scrcpy + ADB)

Uma interface de linha de comando (CLI) simples e poderosa para controlar e espelhar qualquer dispositivo Android diretamente pelo terminal, utilizando o poder do scrcpy e do ADB (Android Debug Bridge).

O objetivo principal deste projeto é: Otimizar o gerenciamento de múltiplos dispositivos ou automatizar o espelhamento de tela sem precisar abrir interfaces gráficas pesadas ou digitar comandos longos toda vez.

## 🔥 Funcionalidades

- 🔌 **Detecção Automática:** Identifica dispositivos conectados via USB ou Wi-Fi.
- 🖥️ **Espelhamento Rápido:** Inicia o scrcpy com configurações otimizadas em um único comando.
- 🎛️ **Controle Total pelo Terminal:** Atalhos integrados para enviar comandos ADB comuns (ligar/desligar tela, tirar screenshot, instalar APKs, etc.).
- 🌐 **Conexão Sem Fio:** Script para emparelhar e conectar o dispositivo via TCP/IP (Wi-Fi) facilmente.
- 🚀 **Modo Performance:** Opções para ajustar a taxa de quadros (FPS), resolução e taxa de bits para conexões mais lentas.

## 🛠️ Pré-requisitos

Antes de iniciar, certifique-se de ter as seguintes ferramentas instaladas no seu sistema operacional:

1. **ADB (Android Debug Bridge):** Como instalar o ADB
2. **Scrcpy:** Repositório Oficial do Scrcpy

### No Android (Dispositivo):

- Ative as Opções do Desenvolvedor no seu celular.
- Ative a Depuração USB.

## 🚀 Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. **Dê permissão de execução (se estiver no Linux/macOS):**
   ```bash
   chmod +x controller.sh
   ```
3. **Execute o script:**
   ```bash
   ./controller.sh
   ```
   *(Nota: Se estiver no Windows usando Prompt/PowerShell, execute o script correspondente .bat ou .ps1)*

## 📖 Como Usar (Exemplos de Comandos)

O script oferece um menu interativo ou aceita argumentos diretos:

- **Listar dispositivos conectados:**
  ```bash
  ./controller.sh --list
  ```
- **Iniciar espelhamento padrão:**
  ```bash
  ./controller.sh --start
  ```
- **Espelhar em baixa resolução (ideal para Wi-Fi):**
  ```bash
  ./controller.sh --low-res
  ```
- **Conectar via Wi-Fi (substitua pelo IP do celular):**
  ```bash
  ./controller.sh --connect 192.168.1.50
  ```

## 🎹 Atalhos Úteis do Scrcpy (Durante o Espelhamento)

Enquanto a tela do celular estiver aberta, você pode usar estes comandos do teclado:

- `Mod + f`: Alternar para tela cheia.
- `Mod + h`: Simular o botão Home.
- `Mod + b`: Simular o botão Voltar.
- `Mod + n`: Abrir a barra de notificações.
- `Mod + p`: Ligar/Desligar a tela (sem encerrar o espelhamento). *(Nota: Mod geralmente é a tecla Alt esquerda no Windows/Linux ou Cmd no macOS).*

## 🤝 Contribuições

Contribuições são sempre bem-vindas! Se você tem ideias para melhorar este terminal controller:

1. Faça um Fork do projeto.
2. Crie uma Branch para sua modificação (`git checkout -b feature/NovaFuncionalidade`).
3. Abra um Pull Request.

## 📄 Licença e Isenção de Responsabilidade

Este projeto está distribuído sob a licença MIT — veja o arquivo LICENSE para mais detalhes.

### ⚠️ AVISO DE ISENÇÃO (Disclaimer)

- Este script é uma ferramenta de automação/interface e não é afiliado ou endossado pela equipe do Android ou da Genymobile.
- O scrcpy e o ADB são projetos independentes e mantêm suas próprias licenças de uso:
  - **ADB (Android SDK Platform-Tools):** Distribuído sob a licença Apache 2.0.
  - **scrcpy:** Distribuído sob a licença Apache 2.0 por Genymobile.
