from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.robots = [Robot("Robo", Weapon("Sword", 8)), Robot("Gizmo", Weapon("Electrical Orb", 20)), Robot("Rusty", Weapon("Laser Beams", 30)), Robot("Tin", Weapon ("Taser", 50))]
    
