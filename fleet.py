from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
    

    def create_fleet(self):
        weapon1 = Weapon("Sword", 8)
        weapon2 = Weapon("Electrical Orb", 20)
        weapon3 = Weapon("Laser Beams", 30)
        weapon4 = Weapon ("Taser", 50)
        
        robot1= Robot("Robo", weapon1)
        robot2 = Robot("Gizmo", weapon2)
        robot3 = Robot("Rusty", weapon3)
        robot4 = Robot("Tin", weapon4)

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
        self.robots.append(robot4)
