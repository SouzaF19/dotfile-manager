"""Core logic for dotfile management."""

import os
import json
import shutil
from pathlib import Path


HOME_DIR = Path.home()
DOTFILES_DIR = Path("~/.dotfiles")
CONFIG_PATH = Path("~/.dotfile_manager.json")


def get_config_path() -> Path:
    """Returns the path to the config file."""
    return Path.home() / ".dotfile_manager.json"


def load_config() -> dict:
    """Loads the config file, returning defaults if not present."""
    if not CONFIG_PATH.exists():
        default_config = {
            "tracked_files": [],
            "backup_dir": str(Path.home() / ".dotfile_backups")
        }
        save_config(default_config)
        return default_config
    return CONFIG_PATH.read_text().json()


def save_config(config: dict):
    """Saves the config to the config file."""
    CONFIG_PATH.write_text(json.dumps(config, indent=4))


def get_tracked_files() -> list:
    """Returns the list of tracked file paths."""
    config = load_config()
    return config.get("tracked_files", [])


def add_tracked_file(relative_path: str) -> bool:
    """Adds a file to the tracked list, resolving it relative to home."""
    abs_path = Path.home() / relative_path
    if not abs_path.exists():
        return False
    
    tracked = get_tracked_files()
    if relative_path in tracked:
        return False  # Already tracked
    
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


def get_all_dotfiles_recursive(root_path: Path) -> list:
    """Recursively finds files in root_path, excluding .git and .dotfile_manager."""
    result = []
    for root, dirs, files in os.walk(root_path):
        # Remove .git and .dotfile_manager from traversal
        dirs[:] = [d for d in dirs if d not in ('.git', '.dotfile_manager')]
        for file in files:
            full_path = os.path.join(root, file)
            # Get relative path from root
            rel_path = os.path.relpath(full_path, root_path)
            result.append(rel_path)
    return result


def sync_files(source_dir: Path, target_dir: Path, tracked_files: list) -> dict:
    """Syncs tracked files from source to target."""
    results = {"copied": 0, "skipped": 0, "errors": 0}
    tracked_set = set(tracked_files)
    
    for rel_path in tracked_files:
        source_file = os.path.join(root_path, rel_path) if root_path else rel_path # Simplified logic for demo
        # Actually, let's keep it simple: copy from HOME to a backup or another dir.
        # For this tool, we will just list and allow the user to copy.
        # This function is a placeholder for the actual logic.
        pass
    return results