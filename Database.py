import psycopg2
import psycopg2.extras

class Database():

    def __init__(self):
        self.conn = psycopg2.connect(database='Music', user='postgres', host='localhost', password='', port=5432)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # NamedTupleCursor
        self.cur.execute("SELECT version()")
        res = self.cur.fetchall()
        print(res)
    
    def getAllMusicSheet(self, column=''):
        if (not column):
            self.cur.execute("""SELECT piece_id, title, c.commonname, type, dateofcreation, difficulty, appreciation, comments 
            FROM piece 
            LEFT JOIN composer AS c 
            ON piece.composer_id = c.composer_id""")
        else:
            self.cur.execute("SELECT " + column + " FROM piece")
        rows = self.cur.fetchall()
        return rows
    
    def insertMusicSheet(self, musicSheet):
        self.cur.execute("""INSERT INTO piece (title, composer_id, type, dateofcreation, difficulty, appreciation, comments)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """, musicSheet.title, musicSheet.composer_id, musicSheet.type, musicSheet.dateofcreation, musicSheet.difficulty, musicSheet.appreciation, musicSheet.comments)
 
    def getAllComposers(self, column='*'):
        self.cur.execute("SELECT " + column + " FROM composer")
        rows = self.cur.fetchall()
        return rows
    
    def __del__(self):
        self.cur.close()
        self.conn.close()


if __name__ == "__main__":
    database = Database()
    rows = database.getAllComposers()
    row = rows[0]
    for key, value in row.items():
        print(key, value)