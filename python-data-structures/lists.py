list = ["this","is","a","list","example"]
print(list)
#Longitud de la lista
print(len(list))
#Indices en la lista
print(range(len(list)))

for item in list:
    print(item)

#Va a iterar por cada índice de la lista
for i in range(len(list)):
    print(i)
    item = list[i]
    print(f"Item of the list: {item}")
    
#Split
numbers = [21,20,3,5877,5,6]
print(numbers[1:3])
print(numbers[:])
print(numbers[:5])
print(numbers[2:])

#Tipo de dato
print(type(numbers))
#Métodos
print(dir(numbers))

#Append: agregar elementos de último en una lista
stuff = []
stuff.append("book")
stuff.append("chair")
print(stuff)

#Método in o not in para saber si un elemento está en una lista
print(9 in stuff)
print("book" in stuff)
print("tables" not in stuff)

#Sort: ordenar
things = ["pen","pencil","ice","cream"]
things.sort()
print(things)

#Len:longitud, min:minimo, max:maximo, sum:suma.
numbers = [21,20,3,5877,5,6]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# #Test

# word_list = []

# while True:
#     word = input("Enter a word: ")
#     if type(word) == str:
#         word_list.append(word)
#         print(word_list)
#     else:
#         print({"message":"error"})

#Split(). Por defecto sin parámetro toma el espacio. Sino, hay que indicarlo.
separate = "Let go to separate this"
separated = separate.split()
print(separated)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
list_data = data.split()
email = list_data[1]
domain = email.split("@")
print(domain[1])

fruit = "Banana"
fruit[0] = "b"
print(fruit)