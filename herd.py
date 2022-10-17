from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()
    

    def create_herd(self):
        dino1 = Dinosaur("Rex", 10)
        dino2 = Dinosaur("Tito", 25)
        dino3 = Dinosaur("Toad", 30)
        dino4 = Dinosaur("Fossil", 55)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)
        self.dinosaurs.append(dino4)
        

