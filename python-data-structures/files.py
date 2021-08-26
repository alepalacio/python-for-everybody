# #Not existing
# file = open("ajdkfj.txt")
# print(file)

#Existing
from os import read


file = open("english.txt")
print(file)

#Reading it
file = open("english.txt")
for letter in file:
    print(letter)

#Reading the whole file
file = open("english.txt")
read_file = file.read()
print(read_file)
print(len(read_file))
print(read_file[:51])

file = open("english.txt")
for line in file:
    if line.startswith("H"):
        print("This line of code: " + line)
        

"""
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fh_read = fh.read()
print(fh_read.upper().rstrip(" "))


"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

fname = input("Enter file name: ")
fh = open(fname)
count = 0
ds_add = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        dspam = line
        dspam_space = dspam.find(" ")
        ds_add += float(dspam[dspam_space:])

average = ds_add / count
print(f"Average spam confidence: {average}")


"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

fname = input("Enter file name: ")
text = open(fname)
count = 0
for lines in text:
    if lines.startswith("From "):
        line = lines.split()
        count = count + 1
        print(line[1])
print(f"There were {count} lines in the file with From as the first word")
        
        
        

