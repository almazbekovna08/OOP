# "Домашнее задание"
# class Animal:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def make_sound(self):
#         pass
#     def display_info(self):
#         pass

# class Lion(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def make_sound(self):
#         print('Рррр!')
#     def display_info(self):
#         print(f'Имя льва - {self.name}, Возраст - {self.age} года')
    
# class Elephant(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def make_sound(self):
#         print('Уууу!')
#     def display_info(self):
#         print(f'Имя слона - {self.name}, Возраст - {self.age} года')


# def introduce_animal(animal):
#     for animals in animal:
#         animals.display_info()
#         animals.make_sound()

# introduce_animal([Lion('Лев', 4), Elephant('Слон', 3)])





# "Практическое задание"
# class Employee:
#     def __init__(self, name, base_stavka):
#         self.name=name
#         self.base_stavka = base_stavka
#     def calculate_salary(self):
#         pass
#     def display_info(self):
#         print(f'Имя сотрудника - {self.name}, Базовая ставка - {self.base_stavka}')
    
# class FullTimeEmployee(Employee):
#     def __init__(self, name, base_stavka):
#         super().__init__(name, base_stavka)
#     def calculate_salary(self):
#         return f'Имя сотрудника - {self.name}, Фиксированная ЗП - {self.base_stavka * 1.2}'


# class PartTimeEmployee(Employee):
#     def __init__(self, name, base_stavka, time):
#         super().__init__(name, base_stavka)
#         self.time=time

#     def calculate_salary(self):
#         return f'Имя сотрудника - {self.name}, Почасовая ЗП - {self.base_stavka * 0.5 * self.time}'
    
# def process_salary(employee):
#     for employees in employee:
#         employees.display_info()
#         print(employees.calculate_salary())

# process_salary([FullTimeEmployee('Adelina', 5000), PartTimeEmployee('Adelina', 5000, 6)])
    

    

    
        