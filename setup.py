from setuptools import setup, find_packages

setup(
    name="dotfile-manager",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "dotfile=dotfile_manager.main:main",
        ],
    },
    author="SouzaF19",
    description="A simple Python tool to track and manage your dotfiles.",
    python_requires=">=3.7",
)
