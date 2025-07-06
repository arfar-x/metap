from abc import ABC, abstractmethod
from typing import TypedDict

# from ..controller import Controller

class InputValue(TypedDict):
    package_name: str


class BaseCommand(ABC):
    @property
    @abstractmethod
    def name() -> str:
        pass
    
    @property
    @abstractmethod
    def help() -> str:
        pass
    
    @abstractmethod
    def register_command(self, subparsers):
        pass
    
    @abstractmethod
    def execute(self, controller):
        pass
    
    @abstractmethod
    def help(self):
        pass
