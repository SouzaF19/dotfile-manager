# README.md

# Dotfile Manager 🛠️

A lightweight Python CLI tool to track, manage, and backup your configuration files (dotfiles) across different environments.

## 🚀 Features

- **Track Files**: Easily add files from your home directory to a tracking list.
- **Automatic Scan**: Detect common dotfiles (like `.bashrc`, `.zshrc`, `.gitconfig`) automatically.
- **Centralized Config**: Keeps a JSON record of all your tracked files.
- **Cross-Platform**: Works on Linux, macOS, and Windows.

## 📦 Installation

### From Source
1. Clone the repository:
   ```bash
   git clone https://github.com/SouzaF19/dotfile-manager.git
   cd dotfile-manager
   ```
2. Install the package:
   ```bash
   pip install .
   ```

## 🛠️ Usage

Once installed, use the `dotfile` command:

| Command | Description | Example |
| :--- | :--- | :--- |
| `init` | Initializes the manager | `dotfile init` |
| `add <file>` | Adds a file to tracking | `dotfile add .bashrc` |
| `list` | Lists all tracked files | `dotfile list` |
| `remove <file>` | Stops tracking a file | `dotfile remove .bashrc` |
| `scan` | Scans for common dotfiles | `dotfile scan` |
| `help` | Shows help menu | `dotfile help` |

## 📁 How it Works

The tool maintains a configuration file at `~/.dotfile_manager.json` which stores the list of files you want to keep track of. This makes it easy to script backups or sync these files to a Git repository.

## 📄 License

MIT License
