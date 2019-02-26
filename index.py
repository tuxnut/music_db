from bottle import Bottle, run, template, debug
from Database import Database

app = Bottle()
db = Database()

@app.route('/')
@app.route('/pieces')
def home():
    piecesArray = db.getAllPieces()
    composersArray = db.getAllComposers()
    composersName = [composer['commonname'] for composer in composersArray]
    return template('pieces', piecesArray=piecesArray, composersArray=composersName)

@app.route('/composers')
def composer():
    composersArray = db.getAllComposers()

debug(True)
run(app, host='localhost', port=8080, reloader=True)
