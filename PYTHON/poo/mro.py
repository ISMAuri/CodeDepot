# Method Resolution Order
"""
    A
   B C    en el orden D > B > C > A; B & C dependen del orden que se les llame
    D                             en D, si C se llamase primero, iria primero
"""
# si B tuviera superclase A y C super clase E e.g. iria en orden:
"""
    A E
    B C    donde D > B > A > C > E
     D 
"""
# ↓ con .mro() podemos ver la jerarquia que sigue dicho metodo ↓


class A:
    def hablar(self):
        print('A')

class B(A):
    def hablar(self):
            print('B')

class C(A):
    def hablar(self):
        print('C')

class D(C, B):
    pass

x = D()

x.hablar()

# si queremos hablar desde, en este caso, B
B.hablar(x)

# ver la jerarquia
print(D.mro())