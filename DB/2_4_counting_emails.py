import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')
cur.execute('''CREATE TABLE Counts(emailt Text, count INTEGER)''')
filename = input('Enter file name: ')
if not filename: filename = 'mbox-short.txt'

fh = open(filename)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # ' ...?' (x, ...) is placeholder and fill like ('...%s' % email)
    cur.execute('''SELECT count FROM Counts WHERE email = ? ''', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) Values (?, 1)''',
                    (email,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE email = ?''',
                    (email,))
        conn.commit()

sqlstr = '''SELECT email, count FROM Counts ORDER BY count DES LIMIT 10'''
for row in cur.execute(sqlstr):
    print(str(row[0], row[1]))

cur.close()
fh.close()
