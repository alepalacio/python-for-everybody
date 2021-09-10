import re

"""
Using re.search() as find()
"""

text = open('mbox-short.txt')

for line in text:
    line = line.strip()
    if re.search('From:', line):
        print(line)
    
"""
Using re.search() as startswith()
"""
text = open('mbox-short.txt')

for line in text:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
        
"""
Using special characters. * is any number of times
"""

text = open('mbox-short.txt')

for line in text:
    line = line.rstrip()
    if re.search('^X.*:', line):
        print(line)

"""
Using special characters.
"""

text = open('mbox-short.txt')

for line in text:
    line = line.rstrip()
    if re.search('^X-\S+:', line):
        print('Second type of chars:', line)