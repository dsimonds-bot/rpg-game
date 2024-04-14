# Package Import
from abc import ABC, abstractmethod

class baseClass(ABC):

    base_armor=0
    base_attack=0
    base_speed=0

    def __init__(self, **kwargs) -> None:
        
        # Base attributes
        self.total_armor = self.base_armor
        self.total_attack = self.base_attack
        self.total_speed = self.base_speed
        
        return None

    def bonus_armor(self, bonus_amt:int=0):
        self.total_armor += bonus_amt

    def bonus_attack(self, bonus_amt:int=0):
        self.total_attack += bonus_amt

    def bonus_speed(self, bonus_amt:int=0):
        self.total_speed += bonus_amt