class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.attack_type = ("Claw", "Chomp", "Body Slam", "Round House Kick")

    def attack_robot(self, robot_to_attack):
       if self.health > 0:
            while True:
                try:
                    attack_choice = int(input(f'Choose attack type: (1) {self.attack_type[0]}, (2) {self.attack_type[1]}, (3) {self.attack_type[2]}, or (4) {self.attack_type[3]}'))
                except ValueError:
                    continue
                if attack_choice == 1:
                    print(f'{self.name} attacked {robot_to_attack.name} with {self.attack_type[0]}')
                    robot_to_attack.health -= self.attack_power
                    print(f'{self.name} energy is now {self.health}')
                    print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')
                if attack_choice == 2:
                    print(f'{self.name} attacked {robot_to_attack.name} with {self.attack_type[1]}')
                    robot_to_attack.health -= self.attack_power
                    print(f'{self.name} energy is now {self.health}')
                    print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')
                if attack_choice == 3:
                    print(f'{self.name} attacked {robot_to_attack.name} with {self.attack_type[2]}')
                    robot_to_attack.health -= self.attack_power
                    print(f'{self.name} energy is now {self.health}')
                    print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')
                if attack_choice == 4:
                    print(f'{self.name} attacked {robot_to_attack.name} with {self.attack_type[3]}')
                    robot_to_attack.health -= self.attack_power
                    print(f'{self.name} energy is now {self.health}')
                    print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')
        if self.health <=0:
            print ('Your Dinosaur has been defeated.')
        if robot_to_attack.health <=0:
            print ('You defeated the robot!')
    

            

        # robot_to_attack.health -= self.attack_power
        # print(f'{self.name} energy is now {self.health}')
        # print(f'{robot_to_attack.name} health is now {robot_to_attack.health}')




