# class Computer:
#     def __init__(self, cpu, memory):
#         self.__cpu=cpu
#         self.__memory=memory
#     def __make_conputations(self):
#         results = (f"""{self.__cpu} + {self.__memory} = {self.__cpu + self.__memory}
# {self.__cpu} - {self.__memory} = {self.__cpu - self.__memory}
# {self.__cpu} * {self.__memory} = {self.__cpu * self.__memory}
# {self.__cpu} / {self.__memory} = {self.__cpu / self.__memory}""")
#         return results

#     @property
#     def cpu(self):
#         return self.__cpu
    
#     @property
#     def memory(self):
#         return self.__memory
    
#     def info(self):
#         print (f'Центральный процессор - {self.cpu}, Память - {self.memory} гб')

#     def compute(self):
#         return self.__make_conputations()
    
# cp=Computer(3.4, 16)
# cp.info()
# print(cp.compute())


# class Laptop(Computer):
#     def __init__(self, cpu, memory, memory_card):
#         super().__init__(cpu, memory)
#         self.__memory_card=memory_card

#     @property
#     def memory_card(self):
#         return self.__memory_card
    
#     def info(self):
#         print (f'Центральный процессор - {self.cpu}, Память - {self.memory} гб, Карта памяти - {self.memory_card}')

# lp=Laptop(2.9, 8, 'SD')
# lp.info()
# print(lp.compute())



    

    
