from BaseDatabase import BaseDatabase
import psycopg2
import psycopg2.extras
import os

class PostgreSQLDb(BaseDatabase):

    scoreTableName = "score"
    composerTableName = "composer"

    def __init__(self):
        # Booleans to query database
        self.updateComposerTable = True
        self.updateScoreTable = True
        # Cache dictionnaries for tables
        self.musicScoreCache = {}
        self.composerCache = {}
        # Connection and Cursor provided by psycopg2
        self.conn = psycopg2.connect(database=os.getenv("DB_NAME"), user=os.getenv("DB_USER"), host=os.getenv("DB_HOSTNAME"), password=os.getenv("DB_PASSWORD"), port=os.getenv("DB_PORT"))
        self.conn.set_session(autocommit=True)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor) # NamedTupleCursor
        self.cur.execute("SELECT version()")
        res = self.cur.fetchall()
        print(res)
    
    def getAllMusicScore(self, column=''):
        # No need to query database if no insert / update was performed since last select
        if (self.updateScoreTable):
            if (not column):
                self.cur.execute("""SELECT score_id, title, c.commonname, type, dateofcreation, difficulty, appreciation, comments 
                FROM score 
                LEFT JOIN composer AS c 
                ON score.composer_id = c.composer_id""")
            else:
                self.cur.execute("SELECT " + column + " FROM score")
            self.musicScoreCache = self.cur.fetchall()
            self.updateScoreTable = False
        return self.musicScoreCache
    
    def insertMusicScore(self, musicScore):
        insertQuery = "INSERT INTO " + self.scoreTableName + "(title, composer_id, type, "
        valueQuery = "VALUES (%(title)s, %(composer)s, %(type)s, "
        if musicScore["dateofcreation"] is not None:
            insertQuery += "dateofcreation, "
            valueQuery += "%(dateofcreation)s, "
        insertQuery += "difficulty, appreciation, comments)"
        valueQuery += "%(difficulty)s, %(appreciation)s, %(comments)s);"
        query = insertQuery + valueQuery
        self.cur.execute(query, musicScore)
        self.updateScoreTable = True
 
    def getAllComposers(self, column='*'):
        # No need to query database if no insert / update was performed since last select
        if (self.updateComposerTable):
            print("update composer Table") # for debug purpose
            self.cur.execute("SELECT " + column + " FROM composer")
            self.composerCache = self.cur.fetchall()
            self.updateComposerTable = False
        return self.composerCache

    def insertComposer(self, composer):
        insertQuery = "INSERT INTO " + self.composerTableName + "(commonname, fullname, "
        valueQuery = "VALUES (%(name)s, %(fullname)s, "
        if composer["dateofbirth"] is not None:
            insertQuery += "dateofbirth, "
            valueQuery += "%(dateofbirth)s, "
        if composer["dateofdeath"] is not None:
            insertQuery += "dateofdeath, "
            valueQuery += "%(dateofdeath)s, "
        insertQuery += "nationality, style)"
        valueQuery += "%(nationality)s, %(style)s);"
        query = insertQuery + valueQuery
        self.cur.execute(query, composer)
        self.updateComposerTable = True

    def __del__(self):
        if (hasattr(self, 'cur')):
            self.cur.close()
        if (hasattr(self, 'conn')):
            self.conn.close()

if __name__ == '__main__':
    print(os.getenv("DB_NAME"))
    print(os.getenv("DB_HOSTNAME"))
    print(os.getenv("DB_PORT"))
    print(os.getenv("DB_USER"))
    print(os.getenv("DB_PASSWORD"))