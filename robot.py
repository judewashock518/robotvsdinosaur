from weapon import Weapon

class Robot:
    def __init__(self, name, Weapon):
        self.name = name
        self.health = 100
        self.weapon = Weapon
        self.weapon_choice = ['Sword', 'Electrical Orb', 'Laser Beams', 'Taser']


    def attack_dinosaur(self, dinosaur_to_attack):
        if self.health > 0:
            while True:
                try:
                    weapon_choice = int(input(f'Choose your weapon: (1) {self.weapon_choice[0]}, (2) {self.weapon_choice[1]}, (3) {self.weapon_choice[2]}, or (4) {self.weapon_choice[3]}'))
                except ValueError:
                    continue
                if weapon_choice == 1:
                    self.weapon = Weapon("Sword", 8)
                    print(f'{self.name} attacked {dinosaur_to_attack.name} with {self.weapon_choice[0]}')
                    dinosaur_to_attack.health -= self.weapon.attack_power
                    print(f'{self.name} energy is now {self.health}')
                    print (f'{dinosaur_to_attack.name} health is now {dinosaur_to_attack.health}')
                    break
                if weapon_choice == 2:
                    self.weapon = Weapon("Electrical Orb", 20)
                    print(f'{self.name} attacked {dinosaur_to_attack.name} with {self.weapon_choice[1]}')
                    dinosaur_to_attack.health -= self.weapon.attack_power
                    print(f'{self.name} energy is now {self.health}')                    
                    print (f'{dinosaur_to_attack.name} health is now {dinosaur_to_attack.health}')
                    break 
                if weapon_choice == 3:
                    self.weapon = Weapon("Laser Beams", 30)
                    print(f'{self.name} attacked {dinosaur_to_attack.name} with {self.weapon_choice[2]}')
                    dinosaur_to_attack.health -= self.weapon.attack_power
                    print(f'{self.name} energy is now {self.health}')
                    print (f'{dinosaur_to_attack.name} health is now {dinosaur_to_attack.health}')
                    break
                if weapon_choice == 4:
                    self.weapon = Weapon("Taser", 50)
                    print(f'{self.name} attacked {dinosaur_to_attack.name} with {self.weapon_choice[3]}')
                    dinosaur_to_attack.health -= self.weapon.attack_power
                    print(f'{self.name} energy is now {self.health}')
                    print (f'{dinosaur_to_attack.name} health is now {dinosaur_to_attack.health}')
                    break


    

        # dinosaur_to_attack.health -= self.weapon.attack_power
        # print(f'{self.name} energy is now {self.health}')
        # print (f'{dinosaur_to_attack.name} health is now {dinosaur_to_attack.health}')






