import dinosaur
import robot
from fleet import Fleet
from herd import Herd
import random

class Battlefield():
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    def run_game(self):
        self.display_welcome()
        self.robot = self.choose_robot()
        self.dinosaur = self.choose_dinosaur()
        self.battle()
        self.current_turn(self.choose_robot, self.choose_dinosaur)


    def display_welcome(self):
        print('Robot vs Dinosaurs!')

        print('In this game, Robots and Dinosaurs fight to the death.')
        print('Robots belong to a Fleet and Dinosaurs belong to a Herd.')
        print('In order to declare a winner, one or the other has to have 0 health left.')
        print('Good luck!')


    # def choose_team(self):
    #     choose_team = int(input('Choose your team: (1) Robots or (2) Dinosaurs'))
    #     if choose_team == 1:
    #         print('You chose the Robot fleet!')
    #         return choose_team
    #     elif choose_team == 2:
    #         print('You chose the herd of Dinosaurs!')
    #         return choose_team
    #     else:
    #         print('Try input again.')
    #         self.choose_team()

    def choose_robot(self):
        choose_robot = int(input(f"'Choose your robot: (0){self.fleet.robots[0].name}, (1){self.fleet.robots[1].name}, (2){self.fleet.robots[2].name}, (3){self.fleet.robots[3].name}'"))
        if choose_robot == 0:
            print('You chose Robo!')
            return choose_robot
        elif choose_robot == 1:
            print('You chose Gizmo!')
            return choose_robot
        elif choose_robot == 2:
            print('You chose Rusty!')
            return choose_robot
        elif choose_robot == 3:
            print('You chose Tin!')
            return choose_robot
        else:
            print('Oops! Try again.')
            self.choose_robot()

    def choose_dinosaur(self):
        choose_dinosaur = int(input(f"'Choose your dinosaur: (0){self.herd.dinosaurs[0].name}, (1){self.herd.dinosaurs[1].name}, (2){self.herd.dinosaurs[2].name}, (3){self.herd.dinosaurs[3].name}'"))
        if choose_dinosaur == 0:
            print('You chose Rex!')
            return choose_dinosaur
        if choose_dinosaur == 1:
            print('You chose Tito!')
            return choose_dinosaur
        if choose_dinosaur == 2:
            print('You chose Toad!')
            return choose_dinosaur
        if choose_dinosaur == 3:
            print('You chose Fossil!')
            return choose_dinosaur
        else:
            print('Oops! Try again.')
            self.choose_dinosaur()

    def battle(self):
        first_turn = random.randint(1, 2)
        if first_turn == 1:
            print('Robots go first!')
            first_turn = 1
        if first_turn == 2:
            print('Dinosaurs go first!')
            first_turn = 2

    def current_turn(self):

