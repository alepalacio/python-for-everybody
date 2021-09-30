import re

sum = 0
text = open('test.txt', 'r')
numbers = 0

for line in text:
    items = re.findall('[0-9]+', line)
    if items == []:
        continue
    else:
        for num in items:
            sum += int(num)
print(sum)