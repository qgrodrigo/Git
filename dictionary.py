'''
    file title: dictionary.py
    description: metodos de tuplas y diccionarios
    datetime: 09/09/2025 17:54
    autor: cusco    
'''

#tuplas
my_tuple = (2, 1, 2, 6, 7, 2, 9)
print(my_tuple[0])
print(my_tuple[1])

# count(elemento): 
# devuelve el número de veces que aparece un elemento en la tupla. 
print(my_tuple.count(2))

#index(elemento): 
# devuelve el índice de la primera aparición de un elemento en la tupla. 
# Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 
print(my_tuple.index(6))

#len(tupla): 
# aunque no es un método de tupla propiamente dicho, 
# esta función incorporada devuelve la longitud de la tupla.
print(len(my_tuple))

# diccionarios
'''
keys(): devuelve una vista de todas las claves del diccionario.
values(): devuelve una vista de todos los valores del diccionario.
items(): devuelve una vista de todos los pares clave-valor del diccionario.
update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.
'''
person = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

print(person.keys())
print(person.values())
print(person.items())

person.update({"profesión": "ingeniero"})
print(person)