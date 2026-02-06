# task_00_abc.py
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self) -> str:
        pass


class Dog(Animal):
    def sound(self) -> str:
        return "Bark"


class Cat(Animal):
    def sound(self) -> str:
        return "Meow"
