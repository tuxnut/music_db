from bottle import Bottle, run, template, debug, request, redirect, static_file, error
from DatabaseService import DatabaseService, retrieveFamilyName

db = DatabaseService()
app = Bottle()

@app.route('/')
@app.route('/scores')
def home():
    musicScoresArray = db.getAllMusicScores()
    composersArray = db.getAllComposers()
    composersName = [composer['commonname'] for composer in composersArray]
    composersName.sort(key=retrieveFamilyName)
    return template('scores', musicScoresArray=musicScoresArray, composersArray=composersName)

@app.route('/composers', method='get')
def composer():
    composersArray = db.getAllComposers()
    return template('composers', composersArray=composersArray)

@app.route('/composers', method='post')
def postComposer():
    composer = {}
    composer["commonname"] = request.forms.name
    composer["fullname"] = request.forms.fullname
    composer["dateofbirth"] = request.forms.get('dateOfBirth') if request.forms.get('dateOfBirth') is not "" else None
    composer["dateofdeath"] = request.forms.get('dateOfDeath') if request.forms.get('dateOfDeath') is not "" else None
    composer["nationality"] = request.forms.nationality
    composer["style"] = request.forms.style
    db.insertComposer(composer)
    redirect("/composers")

@app.route('/<filename:path>')
def static(filename):
    return static_file(filename, root='static/')

@error(404)
def error404(error):
    return "Nope"

run(app, host='0.0.0.0', port=8080)
