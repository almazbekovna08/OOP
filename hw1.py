# """Задание 1:
# Создайте класс Fruits c атрибутами - (name, color, weight)
# Создайте три объекта класса и с помощью метода выведите информацию о каждом фрукте 
# """
# class Fruits:
#     def __init__(self, name, color, weight):
#         self.name=name
#         self.color=color
#         self.weight=weight
#     def info(self):
#         print(f'Название фрукта - {self.name}, Цвет - {self.color},  Вес - {self.weight}')
# fruit1=Fruits('Яблоко', 'Красное', '30г')
# fruit2=Fruits('Банан', 'Желтый', '20г')
# fruit3=Fruits('Мандарин', 'Оранжевый', '10г')
# fruit1.info()
# fruit2.info()
# fruit3.info()


"""Задание 2:
Создайте класс Book с атрибутами title (название), author (автор) и pages (количество страниц). 
Добавьте метод check_pages, который будет выводить сообщение о том, является ли книга 
тонкой (менее 100 страниц), средней (100-300 страниц) или толстой (более 300 страниц).
"""
# class Book:
#     def __init__(self, title, author, pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def info(self):
#         print(f'Название - {self.title}, Автор - {self.author}, Кол-во страниц - {self.pages}')
#     def check_pages(self):
#         if self.pages>300:
#             print('Книга - толстая')
#         if 100<=self.pages<=300:
#             print('Книга - средняя')
#         if self.pages<100:
#             print('Книга - тонкая')
# book=Book('Цветы для Элджернона', 'Даниел Киз', 56 )
# book.info()
# book.check_pages()
        
        
    
        
