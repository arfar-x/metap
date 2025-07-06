from .base import BaseCommand, InputValue
# from ..controller import Controller


class InstallCommand(BaseCommand):
    name: str = "install"
    
    help: str = "Install a package"
    
    def register_command(self, subparsers):
        subparser = subparsers.add_parser(self.name, help=f"{self.name.capitalize()} a package")
        subparser.add_argument("package", help="Package name to install")
        return subparser
    
    def execute(self, controller):
        input_obj = InputValue(package_name=self.package_name)
        result = controller.run(input_obj)
        if not result:
            print(f"Could not install package '{self.package_name}'.")
        else:
            controller.add_to_dependencies(self.package_name, "*")
            print(f"Package '{self.package_name}' installed successfully.")
    
    def help(self):
        pass