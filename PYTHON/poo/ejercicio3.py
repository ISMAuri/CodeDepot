class Personajes:
    def __init__(self, nombre, velocidad, fuerza):
        self.nombre = nombre
        self.velocidad = velocidad
        self.fuerza = fuerza
    
    def __repr__(self):
        return f'{self.nombre} (velocidad: {self.velocidad}, fuerza: {self.fuerza})'
    
    def __add__(self, otro):
        n = self.nombre + '-' + otro.nombre
        v = round(((self.velocidad + otro.velocidad)/2)**1.3)
        f = round(((self.fuerza + otro.fuerza)/2)**1.3)
        return Personajes(n , v , f)
    

isma = Personajes('Ismael', 20, 40)
satoru = Personajes('Random', 120, 120)

print(isma + satoru)