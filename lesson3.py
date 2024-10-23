# "Инкапсуляция"

# class PublicEx:
#     def __init__(self, value):
#         self.value=value #публичный атрибут
#     def info(self):
#         return self.value
# public=PublicEx(32)
# # print(public.info())
# # print(public.value)

# class ProtectedEx:
#     def __init__(self, value):
#         self._value=value #защищенный атрибут
#     def _info(self):
#         return self._value #защищенный метод
# protected=ProtectedEx(100)
# print(protected._info) #это работает, но противоречит принципам инкапсуляции
# print(protected._value) #можно получить значение на прямую, но не рекомендуется

# class ExampleProt(ProtectedEx):
#     def __init__(self, value):
#         super().__init__(value)
# examp= ExampleProt(300)
# print(examp._info())
# print(examp._value)

# class PrivatEx:
#     def __init__(self, value):
#         self.__value=value #приватный атрибут

#     def __info(self):
#         return f'Приватный класс {self.__value}' #приватный метод
#     def access_private(self):
#         return self.__info() #публичный метод, где мы получаем доступ к приватному методу или атрибуту
    
# priv=PrivatEx(200)
# # print(priv.__info()) #прямой вызов приватного метода - ошибка

# # print(priv.__value) #прямой вызов приватного атрибута - ошибка

# print(priv.access_private()) #доступ при помощи публичного метода

# print(priv._PrivatEx__value)
# print(priv._PrivatEx__info()) #доступ к приватному методу или атрибуту через name mangling




# import datetime
# class Car:
#     def __init__(self, marka, model, year, mileage):
#         self.marka=marka
#         self.model=model
#         self.__year=year
#         self.__mileage=mileage
#     def info(self):
#         return f'Марка - {self.marka} \nМодель - {self.model}'
    
#     def _calculate_age(self):
#         current=datetime.datetime.now().year
#         return f'Возраст машины - {current - self.__year}'
    
#     def __update_mileage(self):
#         print(f'Мили - {self.__mileage}')

#     def set_mileage(self):
#         return self.__update_mileage()
# car=Car('BMW', 'X5', 2020, 240000)
# print(car.info())
# print(car._calculate_age())
# # print(car.__update_mileage())
# print(car.set_mileage())




         
        

