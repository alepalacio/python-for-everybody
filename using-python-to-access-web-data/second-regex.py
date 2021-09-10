"""
Extracting data
"""
import re

text = 'My favourite numbers are 24, 48 and also 1987'

extracted = re.findall('[0-9]+', text)
print(extracted)


extracted = re.findall('[AEIOU]', text)
print('Empty list', extracted)

# """
# mbox-short.txt 
# """

# text = open('mbox-short.txt')

# for line in text:
#     line = line.rstrip()
#     if re.findall('[0-9]+', line):
#         print(line)


"""
Greedy matching
"""
text = 'From: Using the: character'

extracted = re.findall('^F.+:', text)
print(extracted)

"""
Non-greedy matching.  (. any character), (+ one or more times), (? don't be greedy)
"""
text = 'From: Using the: character'

extracted = re.findall('^F.+?:', text)
print(extracted)

"""
Extracting email.
"""

text = 'From: alecsand@gmail.com to a new boss'

extracted = re.findall('\S+@\S+', text)
print(extracted)

# text = open('mbox-short.txt')

# for line in text:
#     line = line.rstrip()
#     if re.findall('\S+@\S+', line):
#         print(line)

extracted = re.findall('^From: (\S+@\S+)', text)
print(extracted)

"""
Extracting domain. [] match non-blank character.
"""
text = 'From: alecsand@gmail.com to a new boss'

extracted = re.findall('@([^ ]*)', text)
print(type(extracted))