import re

sum = 0
items = 0
text = open('regex-sum.txt', 'r')

for line in text:
    items = re.findall('[0-9]+', line)
    if items == []:
        continue
    else:
        for num in items:
            sum += int(num)
print(sum)

# numbers = list()
# text = open('regex-sum.txt')

# for line in text:
#     line = line.rstrip()
#     for numbers in line:
#         if re.findall('([0-9])+', numbers):
#             print(numbers)