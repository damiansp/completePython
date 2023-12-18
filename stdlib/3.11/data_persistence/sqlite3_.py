import sqlite3


DB_NAME = 'tutorial.db'


def main():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    init_table(cur)
    verify_table(cur)
    insert(cur, conn)
    query(cur)
    insert_many(cur, conn)
    show_many(cur)
    conn, cur = verify_data_on_disk(conn)
    

def init_table(cur):
    create = 'CREATE TABLE movie(title, year, score)'
    cur.execute(create)


def verify_table(cur):
    q = 'SELECT name FROM sqlite_master'
    res = cur.execute(q)
    print('res:', res.fetchone())
    nosuch_q = "SELECT name FROM sqlite_master WHERE name='spam'"
    res = cur.execute(nosuch_q)
    print('Table "spam" exists:', res.fetchone() is not None)


def insert(cur, conn):
    q = '''
        INSERT INTO movie VALUES
          ('Monty Python and the Holy Grail', 1975, 8.2),
          ('And Now for Something Completely Different', 1971, 7.5);'''
    cur.execute(q)
    conn.commit()


def query(cur):
    insert_q = 'SELECT score FROM movie'
    res = cur.execute(insert_q)
    print('res:', res.fetchall())


def insert_many(cur, conn):
    data = [
        ('Monty Python Live at the Hollywood Bowl', 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0)]
    insert_q = 'INSERT INTO movie VALUES(?, ?, ?)'
    cur.executemany(insert_q, data)
    conn.commit()


def show_many(cur):
    q = 'SELECT year, title FROM movie ORDER BY year'
    for row in cur.execute(q):
        print(row)


def verify_data_on_disk(conn):
    conn.close()
    new_conn = sqlite3.connect(DB_NAME)
    new_cur = new_conn.cursor()
    q = 'SELECT title, year FROM movie ORDER BY score DESC'
    res = new_cur.execute(q)
    title, year = res.fetchone()
    print(f'Best Monty Python movie: {title!r} ({year})')
    return new_conn, new_cur


if __name__ == '__main__':
    main()
