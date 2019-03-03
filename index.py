from bottle import Bottle, run, template, debug, request, redirect, static_file, error
from Database import Database

app = Bottle()
db = Database()

@app.route('/')
@app.route('/sheets')
def home():
    musicSheetsArray = db.getAllMusicSheet()
    composersArray = db.getAllComposers()
    composersName = [{"id": composer['composer_id'], "name": composer['commonname']} for composer in composersArray]
    return template('sheets', musicSheetsArray=musicSheetsArray, composersArray=composersName)

@app.route('/sheets', method='post')
def postMusicSheet():
    musicSheet = {}
    musicSheet["title"] = request.forms.title
    musicSheet["composer"] = request.forms.composer_id
    musicSheet["type"] = request.forms.type
    musicSheet["dateofcreation"] = request.forms.get('dateOfCreation') if request.forms.get('dateOfCreation') is not None else None
    musicSheet["difficulty"] = request.forms.get('difficulty')
    musicSheet["appreciation"] = request.forms.get('appreciation')
    musicSheet["comments"] = request.forms.comments
    db.insertMusicSheet(musicSheet)
    redirect("/sheets")

@app.route('/composers', method='get')
def composer():
    composersArray = db.getAllComposers()
    return template('composers', composersArray=composersArray)

@app.route('/composers', method='post')
def postComposer():
    composer = {}
    composer["name"] = request.forms.name
    composer["fullname"] = request.forms.fullname
    composer["dateofbirth"] = request.forms.get('dateOfBirth') if request.forms.get('dateOfBirth') is not None else None
    composer["dateofdeath"] = request.forms.get('dateOfDeath') if request.forms.get('dateOfDeath') is not None else None
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
