# Dotfile Manager 🛠️

Uma ferramenta leve de CLI em Python para rastrear, gerenciar e fazer backup de seus arquivos de configuração (dotfiles) em diferentes ambientes.

## 🚀 Funcionalidades

- **Rastrear Arquivos**: Adicione facilmente arquivos do seu diretório home a uma lista de rastreamento.
- **Varredura Automática**: Detecta automaticamente dotfiles comuns (como `.bashrc`, `.zshrc`, `.gitconfig`).
- **Configuração Centralizada**: Mantém um registro JSON de todos os seus arquivos rastreados.
- **Multiplataforma**: Funciona em Linux, macOS e Windows.

## 📦 Instalação

### A partir do código-fonte
1. Clone o repositório:
   ```bash
   git clone https://github.com/SouzaF19/dotfile-manager.git
   cd dotfile-manager
   ```
2. Instale o pacote:
   ```bash
   pip install dotf-manage
   ```

## 🛠️ Como Usar

Após a instalação, utilize o comando `dotfile`:

| Comando | Descrição | Exemplo |
| :--- | :--- | :--- |
| `init` | Inicializa o gerenciador | `dotfile init` |
| `add <arquivo>` | Adiciona um arquivo ao rastreamento | `dotfile add .bashrc` |
| `list` | Lista todos os arquivos rastreados | `dotfile list` |
| `remove <arquivo>` | Remove o rastreamento de um arquivo | `dotfile remove .bashrc` |
| `scan` | Varre em busca de dotfiles comuns | `dotfile scan` |
| `help` | Mostra o menu de ajuda | `dotfile help` |

## 📁 Como Funciona

A ferramenta mantém um arquivo de configuração em `~/.dotfile_manager.json` que armazena a lista de arquivos que você deseja monitorar. Isso facilita a criação de scripts de backup ou a sincronização desses arquivos em um repositório Git.

## 📄 Licença

Licença MIT
