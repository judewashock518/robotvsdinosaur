import dinosaur
import robot
from fleet import Fleet
from herd import Herd

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

