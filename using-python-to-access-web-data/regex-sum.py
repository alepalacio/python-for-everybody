import re

numbers = list()
text = open('regex-sum.txt')

for line in text:
    line = line.rstrip()
    for numbers in line:
        if re.findall('([0-9])+', numbers):
            print(numbers)