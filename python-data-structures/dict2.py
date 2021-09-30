fname = input('Enter a file name: ')
file = open(fname)
di = dict()
bigcount = None
bigword = None

for line in file:
    line = line.split()
    
    for word in line:
        if word in line:
            di[word] = di.get(word,0)+1

for key,value in di.items():
    if bigcount is None or value > bigcount:
        bigcount = value
        bigword = key
print(bigword,bigcount)
