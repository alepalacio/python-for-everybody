tup = ('Alex','Emm','Daff','Cesar')
print(tup[0])

# print(dir(tuple()))

# print(dir(tup))

(x,y) = ('Ale',('Jose','Palacio'))
print(x)
print(y)
print(type(x))
print(type(y))

#Con .items() nos devuelve una lista de tuplas.
di = dict()
di['first_name'] = 'Alejandro'
di['last_name'] = 'Palacio'
#print(di.items())
tup = di.items()
print(tup)

for key,value in tup:
    print(key,value)
    
"""
OPERADORES DE COMPARACIÓN
"""
#Si comparamos dos tuplas, al conseguir los elementos que difieran, hace la comparación y no busca más.

x = (1,2,3)
y = (1,3,0)
w = ('Ale', 'Palacio')
z = ('Ale', 'Palacios')

#Devuelve un boolean, en este caso True.
#Compara por índices. x[0]=1, y[0]=1, luego, x[1]=2, y[1]=3. 2 < 3 ? True. Devuelve el boolean y no evalúa el siguiente. Hasta ahí queda.
print(x < y)
print(w > z)

"""
SORT sorted()
"""
#Ordenando por key
d = {'a':10,'b':200,'d':5,'c':47964464564}
print(d)

items = d.items()
print(items)

d_sorted = sorted(items)
print(d_sorted)

for key,value in sorted(d.items()):
    print(f"Key: {key}\nValue: {value}")


#Ordenando por value
c = {'a':10,'b':50,'d':45,'c':7845}
li = list()

for key, value in c.items():
    li.append((value,key))
    print(li)

#Ordenamos la lista de tuplas, y reverse=True, para ordenarlos al revés.    
sorted_li = sorted(li, reverse=True)
print(sorted_li)

"""
PRINTING 10 MOST COMMON WORDS. EXERCISE.
"""
fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'text.txt'

text = open(fname)
t_di = dict()
t_li = list()
sorted_t_li = list()

for line in text:
    words = line.split()
    
    for word in words:
        t_di[word] = t_di.get(word,0)+1

for key,value in t_di.items():
    t_li.append((value,key))
    
sorted_t_li = sorted(t_li, reverse=True)
print(sorted_t_li)

for value,key in sorted_t_li[:10]:
    print(f"Value: {value}, Key: {key}")
    
    
data = ['Pal','Ale','Ser']
data.sort(reverse=True)
print(data)