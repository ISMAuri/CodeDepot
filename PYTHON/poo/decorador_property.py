class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    """Esto no es polimorfismo de sobre carga--definir multiples metodos con el
    mismo nombre pero con diferentes parametros"""
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    @name.deleter
    def name(self):
        del self.__name


persona = Person('Gabriel', 23)

print(persona.name)

persona.name = 'David' # sin el decorador name.setter esto no seria posible

print(persona.name)

print()
print(hasattr(persona, 'name'))
del persona.name # sin name.del esto no seria posible

print()
print(hasattr(persona, 'name'))