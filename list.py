'''
    file title: list.py
    description: métodos de listas
    datetime: 09/09/2025
    autor: cusco
'''

fruits = ["manzana", "banana", "naranja"]

# append(elemento): 
# agrega un elemento al final de la lista.
fruits.append("pera")
print(fruits)

# insert(indice, elemento): 
# inserta un elemento en una posición específica de la lista.
fruits.insert(0, "capulí")
print(fruits)

# remove(elemento): 
# elimina la primera aparición de un elemento en la lista.
fruits.remove("naranja")
print(fruits)

# pop(indice): 
# elimina y devuelve el elemento en una posición específica de la lista.
delete_fruit = fruits.pop(2)
print(fruits)
print(delete_fruit)

#sort(): 
# ordena los elementos de la lista en orden ascendente.
fruits.sort()
print(fruits)

#reverse(): 
# invierte el orden de los elementos en la lista.
fruits.reverse()
print(fruits)