"""Core logic for the Dotfile Manager."""

import os
import json
import shutil
from pathlib import Path

HOME_DIR = Path.home()
CONFIG_PATH = Path.home() / ".dotfile_manager.json"


def get_config() -> dict:
    """Loads or creates the configuration file."""
    if not CONFIG_PATH.exists():
        default_config = {"tracked_files": [], "backup_dir": str(Path.home() / ".dotfile_backups")}
        save_config(default_config)
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)


def save_config(config: dict):
    """Saves the config to the config file."""
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)


def get_tracked_files() -> list:
    """Returns the list of tracked file paths."""
    return load_config().get("tracked_files", [])


def add_tracked_file(relative_path: str) -> bool:
    """Adds a file to the tracked list."""
    abs_path = Path.home() / relative_path
    if not abs_path.exists():
        return False
    tracked = get_tracked_files()
    if relative_path in tracked:
        return False
    tracked.append(relative_path)
    save_config({"tracked_files": tracked})
    return True


def remove_tracked_file(relative_path: str) -> bool:
    """Removes a file from the tracked list."""
    tracked = get_tracked_files()
    if relative_path in tracked:
        tracked.remove(relative_path)
        save_config({"tracked_files": tracked})
        return True
    return False


def list_tracked_files() -> list:
    """Returns the list of tracked files."""
    return get_tracked_files()


# Solicita ao usuário a localização dos dotfiles e adiciona ao rastreamento.
def scan_and_track() -> list:
    """Varre o home directory em busca de arquivos comuns de dotfiles."""
    tracked = []
    common_dotfiles = [
        ".bashrc", ".bashrc_custom", ".zshrc", ".zshrc.zsh",
        ".gitconfig", ".gitconfig.global", ".gitconfig.local",
        ".vimrc", ".ideavimrc", ".tmux.conf",
        ".gitignore_global", ".p10k.zsh",
        ".aliases", ".functions", ".bashrc_aliases",
        ".gitconfig", ".bashrc",
        ".Xresources", ".Xresources.d",
        ".screenrc", ".bashrc",
    ]
    
    for fname in common_dotfiles:
        full_path = Path.home() / fname
        if full_path.exists():
            # Check if it's already tracked
            if fname not in get_tracked_files():
                add_tracked_file(fname)
                tracked.append(fname)
    return tracked