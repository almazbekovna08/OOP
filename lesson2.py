# "Наследование и множественное наследование"

# class Game:
#   def __init__(self, game_name, graphics, game_year, company):
#     self.game_name = game_name
#     self.graphics = graphics  
#     self.game_year = game_year  
#     self.company = company
    
#   def info(self):
#     print(f"Игра - {self.game_name}, Графика - {self.graphics}, Ггод выпуска - {self.game_year}, Компания - {self.company}")
    
# game = Game('MobileLegends', 'Full HD', "2017", "Tencent")
# game.info()

# class Roblox(Game):
#   def __init__(self, game_name, graphics, game_year, company):
#     Game.__init__(self, game_name,graphics, game_year, company)
#     self.multiplayer = 'multiplayer'
#     self.name = 'Iskhak'
#     self.gender = 'man'
#     self.skin = 'naruto'
#     self.hp = '100'
    
#   def info(self):
#     print(f"Game - {self.game_name}, - {self.graphics}, - {self.game_year}, - {self.company}, - {self.multiplayer}")
    
#   def info_player(self):
#     print(f'Player - {self.name}, Gender - {self.gender}, Skin - {self.skin}, Health point - {self.hp}')
    
#   def edit_player(self):
#     name = input('Введите тмя игрока: ')
#     gender = input("Введите пол игрока: ")
#     skin = input("Введите облик")
#     self.name = name
#     self.gender = gender
#     self.skin = skin
  
# roblox = Roblox("Roblox", "ULTRA", "2006", "Roblox_corparatyon")
# roblox.info()
# roblox.edit_player()
# roblox.info_player()

# class Strike(Roblox):
#   def __init__(self, game_name, graphics, game_year, company):
#     super().__init__(game_name, graphics, game_year, company)
#   def info_player(self):
#     return super().info_player()
# st=Strike("Roblox", "ULTRA", "2006", "Roblox_corparatyon")
# st.edit_player()
# st.info_player()


# "Задание практическое"
# class Animal:
#     def __init__(self, name):
#         self.name=name
#     def eat(self):
#         print(f'{self.name} ест')
#     def sleep(self):
#         print(f'{self.name} спит')
# class Walker():
#     def __init__(self, name):
#         self.name=name
#     def walk(self):
#         print(f'{self.name} ходит')
# class Swimmer:
#     def __init__(self, name):
#         self.name=name 
#     def swim(self):
#         print(f'{self.name} плавает')
# class Flyer:
#     def __init__(self, name):
#         self.name=name 
#     def fly(self):
#         print(f'{self.name} летает')


# class Penguin(Animal, Walker, Swimmer ):
#     def __init__(self, name):
#         super().__init__(name)
#     def describe(self):
#         print(f'{self.name} умеет ходить и плавать')


# class Duck(Animal, Walker, Swimmer, Flyer):
#     def __init__(self, name):
#         super().__init__(name)
#     def describe(self):
#         print(f'{self.name} умеет ходить, плавать и летать')

# class Bat(Animal, Flyer):
#     def __init__(self, name):
#         super().__init__(name)
#     def describe(self):
#         print(f'{self.name} умеет летать')



# an1=Penguin('Пингвин')
# an1.walk()
# an1.swim()
# an1.describe()

# an2=Duck('Утка')
# an2.walk()
# an2.swim()
# an2.fly()
# an2.describe()

# an3=Bat('Летучая мышь')
# an3.fly()
# an3.describe()


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i*j:^5}', end=" ")
#     print('')









        





