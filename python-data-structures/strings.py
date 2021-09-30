word = "banana"
found = word.find("a")
print(found)

print(word.upper())
word = word.upper()
print(word.lower())

greet = "Hola Alejandro"
print(greet)
new_greet = greet.replace('Alejandro','Palacio')
print(new_greet)

w = "      Hello dude      "
print(w)
print(w.lstrip())
print(w.rstrip())
print(w.strip())

for char in w:
    print(char)

print(w.startswith('H'))
print(w.startswith(" "))

address = "alejandropalacio@gmail.com "
atfound = address.find("@")
print(atfound)
spfound = address.find(" ")
print(spfound)
domain = address[atfound+1:spfound]
print(domain)

x = 'From marquard@uct.ac.za'
atfound = x.find("@")
print(atfound)
dotfound = x.find(".")
print(dotfound)
domain = x[14:17]
print(domain)

print(len('banana')*7)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

"""
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
"""

text = "X-DSPAM-Confidence:    0.8475"
number = text.find("0")
print(float(text[number:]))