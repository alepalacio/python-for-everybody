"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below
"""

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
text = open(name)
text_di = dict()
text_li = list()

for line in text:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        colon = words[5].split(':')
        text_di[colon[0]] = text_di.get(colon[0],0)+1

for key,value in sorted(text_di.items()):
    print(key,value)