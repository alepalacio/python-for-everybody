"""
Creating a dictionary
"""

from sys import path
from pathlib import Path


new_dict = dict()
new_dict['test'] = "PRUEBA"
new_dict['test2'] = "PRUEBA 2"
print("New dict", new_dict)

if "test" in new_dict:
    print("Found")

"""
Creating a dict
"""

dict_names = dict()    
names = ["Ale","Daffne","Emmanuel","Cesar","Ale"]

for name in names:
    if name in dict_names:
        dict_names[name] = dict_names[name] + 1
    else:
        dict_names[name] = 1

print("For and if", dict_names)

"""
Creating a dict .get()
"""

dict_names = dict()
names = ["Ale","Daffne","Emmanuel","Cesar","Ale","Daffne","Daffne"]


for name in names:
    dict_names[name] = dict_names.get(name, 0) + 1
    #print(dict_names.get(name))
print("Get", dict_names)
#prueba
"""
EJERCICIO CON TEXTO
"""
# counts = dict()
# text = input("Enter some text:")

# words = text.split()

# print("Words:", words)

# for word in words:
#     counts[word] = counts.get(word, 0) + 1
    
# print(counts)

"""
EJERCICIO CON FILES
"""
# counter = dict()
# text = open("mbox-short.txt")
# text_read = text.read()
# lines = text_read.split()

# for word in lines:
#     counter[word] = counter.get(word, 0) + 1
# print(counter)

counter = dict()
text = open("text.txt")
text_read = text.read().lower()
words = text_read.split()


for word in words:
    counter[word] = counter.get(word, 0) + 1
print(counter)

json = {
    "nombre": "Lucia",
    "apellido": "Corral",
    "career": "Engineer",
    "country": "Argentina"
}

# for key in json:
#     print(f"{key} :  {json[key]}")
    
print(list(json))    
print(json.keys())
print(json.values())
print(json.items())

for key,values in json.items():
    print(f"Mi {key} es {values}")


"""
# EJERCICIO DE PRUEBA
# """

# name = input("Enter a file name: ")
# text = open(name)

# counts = dict()

# for line in text:
#     words = line.lower().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# bigcount = None
# bigword = None

# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigcount = count
#         bigword = word
        
# print(f"Biggest word is: '{bigword}' with {bigcount}")

# # stuff = dict()
# # print(stuff['candy'])

# stuff = dict()
# print(stuff.get('candy',-1))

"""
EJERCICIO COURSERA DICT.

9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

name = input("Enter file:")
text = open(name)
counts = dict()
bigcount = None
bigword = None
email = None

for lines in text:
    if lines.startswith("From "):
        line = lines.split()
        email = line[1]
        if email in line:
            counts[email] = counts.get(email,0)+1
print(f"New dict {counts}")

for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigword = key
print(bigword, bigcount)


"""
EJERCICIO DEMOSTRACIÓN CHUCK SEVERANCE
"""

fname = input('Enter a file name: ')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    
    for w in wds:
        #if the key is not there, the count is zero
        # oldcount = di.get(w,0)
        # print(w,'old',oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        
        #todo lo anterior se puede resumir aqui
        di[w] = di.get(w,0)+1
        #print(w,'new',newcount)
print(di)