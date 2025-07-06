import json
from typing import Literal, TypedDict

from .command.base import InputValue
from .extractor import Extractor
from .installer import Installer
from .registry import OfficialRegistry


class ConfigMap(TypedDict):
    registry: dict[str, str]
    dependencies: dict[str, Literal["*"]]
    mt5_path: str
    
    
with open("metap.json", "r", encoding="utf-8") as file:
    config_map = json.load(file)


class Controller:
    def __init__(self):
        self.config_path = "metap.json"
        self.config_map = config_map
        
    def run(self, input: InputValue):
        result = self._autorun(input)
        return result
    
    def _autorun(self, input: InputValue):
        file = OfficialRegistry.get(input["package_name"])
        if not file:
            print("Failed to get the package.")
            return False
        
        extracted_files = Extractor.unzip(file)
        if not extracted_files:
            print("Failed to unzip the package.")
            return False
        
        result = Installer.run(self.config_map["mt5_path"], extracted_files)
        return result
    
    def add_to_dependencies(self, package_name):
        self.config_map["dependencies"]
        
    def write_config_map(self):
        with open(self.config_path, "w") as file:
            json.dump(self.config_map, file, indent=4)


controller = Controller()
