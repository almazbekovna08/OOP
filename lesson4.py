# """Полиморфизм"""
# # num1=1
# # num2=2
# # print(num1+num2)

# # srtring1="Hello world"
# # srtring2="Geeks"
# # print(srtring1+srtring2)

# class Cat:
#     def __init__(self, name, preference):
#         self.name = name
#         self.pref=preference
#     def info(self):
#         print(f'Я кот, меня зовут {self.name}, мне {self.pref} года')
#     def make_sound(self):
#         print('Мяу!')
# class Dog:
#     def __init__(self, name, preference):
#         self.name = name
#         self.pref=preference
#     def info(self):
#         print(f'Я собака, меня зовут {self.name}, мне {self.pref} года')
#     def make_sound(self):
#         print('Гав!')
# cat= Cat('Васька', '3')
# dog= Dog('Muhtar', '4')

# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()

# class PaymentMethod:
#     def pay(self, amount):
#         pass

# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         return f'Сумма {amount}, оплачивается по кредитной карте'
    
# class PayPal(PaymentMethod):
#     def pay(self, amount):
#         return f'Сумма {amount}, оплачивается PayPal'
    
# class BankTransfer(PaymentMethod):
#     def pay(self, amount):
#         return f'Сумма {amount}, оплачивается по банковскому переводу'

# payment=[CreditCard(), PayPal(), BankTransfer()]

# for payments in payment:
#     print(payments.pay(100))


# from abc import abstractmethod

# class Vehicle:
#     def start_engine(self):
#         pass
#     def stop_engine(self):
#         pass
#     def drive(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         return 'Двигатель автомобиля заведен'
#     def stop_engine(self):
#         return 'Двигатель автомобиля не заведен'
#     def drive(self):
#         return 'Автомобиль едет'
    
# class Bicycle(Vehicle):
#     def start_engine(self):
#         return 'У велосипеда нет двигателя'
#     def stop_engine(self):
#         return 'У велосипеда нет двигателя'
#     def drive(self):
#         return 'Велосипед едет'
    
# vehicle=[Car(), Bicycle()]
# for vehicles in vehicle:
#     print(vehicles.start_engine())
#     print(vehicles.stop_engine())
#     print(vehicles.drive())



"Практическое задание"
class Employee:
    def __init__(self, name, base_stavka):
        self.name=name
        self.base_stavka = base_stavka
    def calculate_salary(self):
        pass
    def display_info(self):
        print(f'Имя сотрудника - {self.name}, Базовая ставка - {self.base_stavka}')
    
class FullTimeEmployee(Employee):
    def __init__(self, name, base_stavka):
        super().__init__(name, base_stavka)
    def calculate_salary(self):
        return f'Имя сотрудника - {self.name}, Фиксированная ЗП - {self.base_stavka * 1.2}'


class PartTimeEmployee(Employee):
    def __init__(self, name, base_stavka, time):
        super().__init__(name, base_stavka)
        self.time=time

    def calculate_salary(self):
        return f'Имя сотрудника - {self.name}, Почасовая ЗП - {self.base_stavka * 0.5 * self.time}'
    
def process_salary(employee):
    for employees in employee:
        employees.display_info()
        print(employees.calculate_salary())

process_salary([FullTimeEmployee('Adelina', 5000), PartTimeEmployee('Adelina', 5000, 6)])
    


    




