import sqlite3

#Will create a DB named as written.
conn = sqlite3.connect('example.sqlite')
cur = conn.cursor()

#Avoid duplicated tables
cur.execute('''
DROP TABLE IF EXISTS Counts''')

#Create a table named Counts
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter a file name: ')
if (len(fname) < 1):
    fname = 'mbox-example.txt'

fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    print(pieces)
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()

    if row is None:
        cur.execute('''
        INSERT INTO Counts (email, count) VALUES (?,1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',(email,))

    conn.commit()

# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0], row[1]))

cur.close()
