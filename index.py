from bottle import Bottle, run, template
from Database import Database

app = Bottle()
db = Database()

@app.route('/')
@app.route('/pieces')
def home():
    piecesArray = db.getAllPieces()
    for piece in piecesArray:
        print("id = ", piece[0])
        print("Title = ", piece[1])
        print("Composer = ", piece[2])
        print("Type = ", piece[3])
        print("Creation Data = ", piece[4])
        print("Difficulty = ", piece[5])
        print("Appreciation = ", piece[6])
        print("Comments = ", piece[7])
    return template('pieces', test="Thierry")

@app.route('/composers')
def composer():
    composersArray = db.getAllComposers()
    for composer in composersArray:
        print("id : ", composer[0])
        print("Common name : ", composer[1])
        print("Full name : ", composer[2])
        print("Birth : ", composer[3])
        print("Death : ", composer[4])
        print("Nationality : ", composer[5])
        print("Style : ", composer[6])

run(app, host='localhost', port=8080)
