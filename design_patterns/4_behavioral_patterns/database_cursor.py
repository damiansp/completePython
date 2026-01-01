def main():
    cursor = DatabaseCursor(db_conn, 'SELECT * FROM large_table')
    for row in cursor:
        process_row(row)
        
class DatabaseCursor:
    def __init__(self, conn, query):
        self.conn = conn
        self.q = query
        self.batch_size = 100
        self.offset = 0
        self.cache = []

    def __iter__(self):
        return self

    def __next__(self):
        if not self.cache:
            self._fetch_next_batch()
        if not self.cache:
            raise StopIteration
        return self.cache.pop()

    def _fetch_next_batch(self):
        res = self.conn.execute(
            f'{self.q} LIMIT {self.batch_size} OFFSET {self.offset}')
        self.cache = list(res)
        self.offset += self.batch_size
