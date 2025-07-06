#!/usr/bin/env python3
import argparse

from src.controller import controller
from src.command.base import InputValue

# Simulated package database (for demo purposes)
installed_packages = {}

controller = controller


def install_package(name):
    if name in installed_packages:
        print(f"Package '{name}' is already installed.")
    else:
        print(f"Installing {name}...")
        # Simulate installation logic here
        installed_packages[name] = "1.0.0"
        input = InputValue(package_name=name)
        result = controller.run(input)
        if not result:
            print(f"Could not install package '{name}'.")
        else:
            print(f"Package '{name}' installed successfully.")

def update_package(name):
    if name not in installed_packages:
        print(f"Package '{name}' is not installed.")
    else:
        print(f"Updating {name}...")
        # Simulate update logic here
        print(f"Package '{name}' is up to date.")

def remove_package(name):
    if name in installed_packages:
        print(f"Removing {name}...")
        del installed_packages[name]
        print(f"Package '{name}' removed.")
    else:
        print(f"Package '{name}' is not installed.")

def list_packages():
    if not installed_packages:
        print("No packages installed.")
    else:
        print("Installed packages:")
        for pkg, ver in installed_packages.items():
            print(f"- {pkg} v{ver}")


from src.command import REGISTER_COMMANDS
    
def register_commands(parser: argparse.ArgumentParser, subparsers):
    commands = {}
    for c in REGISTER_COMMANDS:
        c = c()
        subparsers = c.register_command(subparsers)
        commands[c.name] = c
        # subparser = subparsers.add_parser(c.name, help=f"{c.name.capitalize()} a package")
        # subparser.add_argument("package", help=c.help)
    return commands

def main():
    parser = argparse.ArgumentParser(prog="metap", description="MetaTrader 5 Package Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    commands = register_commands(parser, subparsers)

    # Dynamically create subparsers based on COMMANDS
    # for cmd_name, cmd_class in REGISTER_COMMANDS.items():
    #     subparser = subparsers.add_parser(cmd_name, help=f"{cmd_name.capitalize()} a package")
    #     # Only add 'package' argument if the command requires a package name
    #     if cmd_name != "list":
    #         subparser.add_argument("package", help="Package name")

    args = parser.parse_args()
    
    cmd_class = commands.get(args.command)
    if not cmd_class:
        parser.print_help()
        return

    if args.command == "install":
        install_package(args.package)
    elif args.command == "update":
        update_package(args.package)
    elif args.command == "remove":
        remove_package(args.package)
    elif args.command == "list":
        list_packages()
    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()
