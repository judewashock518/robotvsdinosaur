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
        self.team = self.choose_team()
        self.battle()


    def display_welcome(self):
        print('Robot vs Dinosaurs!')

        print('In this game, Robots and Dinosaurs fight to the death.')
        print('Robots belong to a Fleet and Dinosaurs belong to a Herd.')
        print('In order to declare a winner, one or the other has to have 0 health left.')
        print('Good luck!')


    def choose_team(self):
        choose_team = int(input('Choose your team: (1) Robots or (2) Dinosaurs'))
        if choose_team == 1:
            print('You chose the Robot fleet!')
            return choose_team
        elif choose_team == 2:
            print('You chose the herd of Dinosaurs!')
            return choose_team
        else:
            print('Try input again.')
            self.choose_team()
    

    def battle(self):
        first_turn = random.randint(1, 2)
        if first_turn == 1:
            print('Robots go first!')
            first_turn = 1
        if first_turn == 2:
            print('Dinosaurs go first!')
            first_turn = 2

        
