from BaseDatabase import BaseDatabase
import psycopg2
import psycopg2.extras

class PostgreSQLDb(BaseDatabase):
    def __init__(self):
        # Booleans to query database
        self.updateComposerTable = True
        self.updateSheetTable = True
        # Cache dictionnaries for tables
        self.musicSheetCache = {}
        self.composerCache = {}
        # Connection and Cursor provided by psycopg2
        self.conn = psycopg2.connect(database='Music', user='postgres', host='localhost', password='', port=5432)
        self.conn.set_session(autocommit=True)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # NamedTupleCursor
        self.cur.execute("SELECT version()")
        res = self.cur.fetchall()
        print(res)
    
    def getAllMusicSheet(self, column=''):
        # No need to query database if no insert / update was performed since last select
        if (self.updateSheetTable):
            print("update sheet Table") # for debug purpose
            if (not column):
                self.cur.execute("""SELECT piece_id, title, c.commonname, type, dateofcreation, difficulty, appreciation, comments 
                FROM piece 
                LEFT JOIN composer AS c 
                ON piece.composer_id = c.composer_id""")
            else:
                self.cur.execute("SELECT " + column + " FROM piece")
            self.musicSheetCache = self.cur.fetchall()
            self.updateSheetTable = False
        return self.musicSheetCache
    
    def insertMusicSheet(self, musicSheet):
        # Need the composer_id for the FK_composer
        print(musicSheet)
        self.cur.execute("""INSERT INTO piece (title, composer_id, type, dateofcreation, difficulty, appreciation, comments)
        VALUES (%(title)s, %(composer)s, %(type)s, %(dateofcreation)s, %(difficulty)s, %(appreciation)s, %(comments)s);""",
        musicSheet)
        self.cupdateSheetTable = True
 
    def getAllComposers(self, column='*'):
        # No need to query database if no insert / update was performed since last select
        if (self.updateComposerTable):
            print("update composer Table") # for debug purpose
            self.cur.execute("SELECT " + column + " FROM composer")
            self.composerCache = self.cur.fetchall()
            self.updateComposerTable = False
        return self.composerCache

    def insertComposer(self, composer):
        self.cur.execute("""INSERT INTO composer (commonname, fullname, dateofbirth, dateofdeath, nationality, style)
        VALUES (%(name)s, %(fullname)s, %(dateofbirth)s, %(dateofdeath)s, %(nationality)s, %(style)s);""",
        composer)
        self.updateComposerTable = True

    def __del__(self):
        if (hasattr(self, 'cur')):
            self.cur.close()
        if (hasattr(self, 'conn')):
            self.conn.close()


if __name__ == "__main__":
    date = ''
    date = date if date is not None else None
    print(date)