import psycopg2
import psycopg2.extras

class Database():

    def __init__(self):
        self.conn = psycopg2.connect(database='Music', user='postgres', host='localhost', password='', port=5432)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.cur.execute("SELECT version()")
        res = self.cur.fetchall()
        print(res)
    
    def shutDown(self):
        self.conn.close()
    
    def getAllPieces(self):
        self.cur.execute("SELECT piece_id, title, c.commonname, type, dateofcreation, difficulty, appreciation, comments FROM piece LEFT JOIN composer AS c ON piece.composer_id = c.composer_id")
        rows = self.cur.fetchall()
        return rows
    
    def getAllComposers(self):
        self.cur.execute("SELECT * FROM composer")
        rows = self.cur.fetchall()
        return rows


if __name__ == "__main__":
    database = Database()
    rows = database.getAllComposers()
    row = rows[0]
    for key, value in row.items():
        print(key, value)