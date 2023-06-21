# creando conjunto con set()
conjunto = set(["A","Hola",'dato1', 'dato2','dato3'])

#creando conjunto con {}
conjunto = {'dato1', 'dato2','dato3'}

# conjunto dentro de otro conjunto(subconjunto)
conjunto = frozenset({'dato1', 'dato2'})
conjunto1 = {conjunto,'dato3'}
print(conjunto1)

# Teoria de conjuntos

set1 = {1,2,5,7}
set2 = {1,2,7}

resultado1 = set1.issuperset(set2)
resultado1 = set2 < set1 or set1 > set2 #es lo mismo
resultado2 = set2.issubset(set1)
resultado2 = set1 >= set2 or set2 <= set1 # es lo mismo

# verificando si hay algun numero en comun(si es asi, False)

disjointornot = set1.isdisjoint(set2)

print(disjointornot)