# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def start(self):
#         print(f'{self.brand} - заводится')
#     def stop(self):
#         print(f'{self.brand} - останавливается')
#     def info(self):
#         print(f'Марка - {self.brand}, Модель - {self.model}, Год выпуска - {self.year}')


# class Car(Vehicle):
#     def __init__(self, brand, model, year, doors):
#         super().__init__(brand, model, year)
#         self.doors=doors
#     def info(self):
#         print(f'Марка - {self.brand}, Модель - {self.model}, Год выпуска - {self.year}, Кол-во дверей - {self.doors}')
#     def open_trunk(self):
#         print('Багажник открыт')
# car=Car('BMW', 'X5', 2024, 4)
# car.info()
# car.start()
# car.stop()
# car.open_trunk()



# class Bicycle(Vehicle):
#     def __init__(self, brand, model, year, type_of_bicycle):
#         super().__init__(brand, model, year)
#         self.type_of_bc=type_of_bicycle
#     def info(self):
#         print(f'Марка - {self.brand}, Модель - {self.model}, Год выпуска - {self.year}, Тип велосипеда - {self.type_of_bc}')
#     def start(self):
#         print(f'{self.brand} - начинает движение')
#     def stop(self):
#         print(f'{self.brand} - останавливается')
#     def ring_bell(self):
#         print('Звонок звенит')
# bl=Bicycle('Велосипед', 'Pegas', 2018, 'горный')
# bl.info()
# bl.start()
# bl.stop()
# bl.ring_bell()



# class Boat(Vehicle):
#     def __init__(self, brand, model, year, length):
#         super().__init__(brand, model, year)
#         self.length=length
#     def info(self):
#         print(f'Марка - {self.brand}, Модель - {self.model}, Год выпуска - {self.year}, Длина лодки - {self.length}')
#     def start(self):
#         print(f'{self.brand} - отплывает')
#     def stop(self):
#         print(f'{self.brand} - причаливает')
#     def anchor(self):
#         print('Якорь спущен')
# bt=Boat('Лодка', 'Yacht', 2009, '10 метров')
# bt.info()
# bt.start()
# bt.stop()
# bt.anchor()
