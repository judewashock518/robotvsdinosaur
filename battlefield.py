import dinosaur
import robot
from fleet import Fleet
from herd import Herd
import random 


class Battlefield():
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.goes_first = ''


    def run_game(self):
        self.display_welcome()
        self.robot = self.choose_robot()
        self.dinosaur = self.choose_dinosaur()
        self.battle()
        self.current_turn()
        self.display_winner()


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
        choose_robot = int(input(f"Choose your robot: (0){self.fleet.robots[0].name}, (1){self.fleet.robots[1].name}, (2){self.fleet.robots[2].name}, (3){self.fleet.robots[3].name}"))
        if choose_robot == 0:
            print('You chose Robo!')
            return self.fleet.robots[0]
        elif choose_robot == 1:
            print('You chose Gizmo!')
            return self.fleet.robots[1]
        elif choose_robot == 2:
            print('You chose Rusty!')
            return self.fleet.robots[2]
        elif choose_robot == 3:
            print('You chose Tin!')
            return self.fleet.robots[3]
        else:
            print('Oops! Try again.')
            self.choose_robot()

    def choose_dinosaur(self):
        choose_dinosaur = int(input(f"Choose your dinosaur: (0){self.herd.dinosaurs[0].name}, (1){self.herd.dinosaurs[1].name}, (2){self.herd.dinosaurs[2].name}, (3){self.herd.dinosaurs[3].name}"))
        if choose_dinosaur == 0:
            print('You chose Rex!')
            return self.herd.dinosaurs[0]
        if choose_dinosaur == 1:
            print('You chose Tito!')
            return self.herd.dinosaurs[1]
        if choose_dinosaur == 2:
            print('You chose Toad!')
            return self.herd.dinosaurs[2]
        if choose_dinosaur == 3:
            print('You chose Fossil!')
            return self.herd.dinosaurs[3]
        else:
            print('Oops! Try again.')
            self.choose_dinosaur()

    def battle(self):
        first_turn = random.randint(1, 2)
        if first_turn == 1:
            print('Robots go first!')
            self.goes_first = "Robot"
        if first_turn == 2:
            print('Dinosaurs go first!')
            self.goes_first = "Dinosaur"

    def current_turn(self):
        while self.dinosaur.health >0 and self.robot.health >0:

            if self.goes_first == "Robot":
                self.robot.attack_dinosaur(self.dinosaur)
                self.dinosaur.attack_robot(self.robot)
            elif self.goes_first == "Dinosaur":
                self.dinosaur.attack_robot(self.robot)
                self.robot.attack_dinosaur(self.dinosaur)

    def display_winner(self):
        if self.robot.health <=0:
            print(f'{self.robot.name} has defeated {self.dinosaur.name}! {self.robot.name} is the winner!')
        elif self.dinosaur.health <=0:
            print(f'{self.dinosaur.name} has defeated {self.robot.name}! {self.dinosaur.name} is the winner!')

