import sqlite3

#Will create a DB named as written.
conn = sqlite3.connect('mbox.sqlite')
cur = conn.cursor()

#Avoid duplicated tables
cur.execute('''
DROP TABLE IF EXISTS Counts''')

#Create a table named Counts
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#Usin mbox.txt file in local storage
fname = input('Enter a file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'

fh = open(fname)

for lines in fh:
    #Retrieving lines starting with 'From:' only.
    if not lines.startswith('From: '):
        continue
    #Right
    line = lines.rstrip()
    #Spliting by '@'
    pieces = line.split('@')
    #print(pieces)
    domain = pieces[1]
    #print(domain)
    cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
    row = cur.fetchone()

    if row is None:
        cur.execute('''
        INSERT INTO Counts (org, count) VALUES (?,1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(domain,))

    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    #print(row)

cur.close()

