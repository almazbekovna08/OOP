class Person:
    def __init__(self, name, age):
        self._name = name  # Приватное поле
        self._age = age    # Приватное поле

    # Геттер для имени
    @property
    def name(self):
        return self._name

    # Геттер для возраста
    @property
    def age(self):
        return self._age

# Использование
person = Person("Alice", 30)
print(person.name)  # Alice
print(person.age)   # 30
