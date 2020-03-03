from bottle import Bottle, run, template, debug, request, redirect, static_file, error
from PostgreSQLDb import PostgreSQLDb
from LocalDatabase import LocalDatabase

try:
    db = PostgreSQLDb()
except:
    print("Unable to reach database 'Music' at 'postgres@localhost:5432'")
    db = LocalDatabase()

app = Bottle()

@app.route('/')
@app.route('/scores')
def home():
    musicScoresArray = db.getAllMusicScore()
    composersArray = db.getAllComposers()
    composersName = [{"id": composer['composer_id'], "name": composer['commonname']} for composer in composersArray]
    return template('scores', musicScoresArray=musicScoresArray, composersArray=composersName)

@app.route('/scores', method='post')
def postMusicScore():
    musicScore = {}
    musicScore["title"] = request.forms.title
    musicScore["composer"] = request.forms.composer_id
    musicScore["type"] = request.forms.type
    musicScore["dateofcreation"] = request.forms.get('dateOfCreation') if request.forms.get('dateOfCreation') is not "" else None
    musicScore["difficulty"] = request.forms.get('difficulty')
    musicScore["appreciation"] = request.forms.get('appreciation')
    musicScore["comments"] = request.forms.comments
    db.insertMusicScore(musicScore)
    redirect("/scores")

@app.route('/composers', method='get')
def composer():
    composersArray = db.getAllComposers()
    return template('composers', composersArray=composersArray)

@app.route('/composers', method='post')
def postComposer():
    composer = {}
    composer["name"] = request.forms.name
    composer["fullname"] = request.forms.fullname
    composer["dateofbirth"] = request.forms.get('dateOfBirth') if request.forms.get('dateOfBirth') is not "" else None
    composer["dateofdeath"] = request.forms.get('dateOfDeath') if request.forms.get('dateOfDeath') is not "" else None
    composer["nationality"] = request.forms.nationality
    composer["style"] = request.forms.style
    db.insertComposer(composer)
    redirect("/composers")

@app.route('/<filename:path>')
def static(filename):
    print()
    return static_file(filename, root='static/')

@error(404)
def error404(error):
    return "Nope"

debug(True)
run(app, host='localhost', port=8080, reloader=True)
