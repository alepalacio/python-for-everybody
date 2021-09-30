# import math

# def square_root(numbers):
#     result = []
#     for number in numbers:
#         result.append(math.sqrt(number))
#     print(result)
        
# numbers = [1,2,3]
# square_root(numbers)

# def append_list(words):
#     result = []
#     for word in words:
#         listi = word.split()
#         result.append(listi)
#     print(result)
    
# words = "Ale Pal"
# append_list(words)

# text = "Hola soy alejandro"
# new_text = text.split()
# print(new_text)

# ls = list()
# print(type(ls))

"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

fname = input("Enter file name: ")
text = open(fname)


array = []

for line in text:
    #Imprime cada línea
    print(line)
    #Elimino el espacio a la derecha y elimino espacios
    phrases = line.rstrip().split()
    print(phrases)
    #Itero por cada palabra de cada frase
    for word in phrases:
        print(word)
        #Si la palabra está en el array, sigue
        if word in array:
            continue
        #Sino agregalo al array
        else:
            array.append(word)
print(array)