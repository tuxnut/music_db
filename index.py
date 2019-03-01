from bottle import Bottle, run, template, debug, request, redirect, static_file, error
from Database import Database

app = Bottle()
db = Database()

@app.route('/')
@app.route('/sheets')
def home():
    musicSheetsArray = db.getAllMusicSheet()
    composersArray = db.getAllComposers()
    composersName = [composer['commonname'] for composer in composersArray]
    return template('sheets', musicSheetsArray=musicSheetsArray, composersArray=composersName)

@app.route('/sheets', method='post')
def postMusicSheet():
    musicSheet = {}
    musicSheet["title"] = request.forms.get('title')
    musicSheet["composer"] = request.forms.get('composer')
    musicSheet["type"] = request.forms.get('type')
    musicSheet["dateofcreation"] = request.forms.get('dateOfCreation')
    musicSheet["difficulty"] = request.forms.get('difficulty')
    musicSheet["appreciation"] = request.forms.get('appreciation')
    musicSheet["comments"] = request.forms.get('comments')
    print(musicSheet)
    redirect("/sheets")

@app.route('/composers', method='get')
def composer():
    composersArray = db.getAllComposers()
    return template('composers', composersArray=composersArray)

@app.route('/composers', method='post')
def postComposer():
    composer = {}
    composer["name"] = request.forms.get('name')
    composer["fullname"] = request.forms.get('fullname')
    composer["dateofbirth"] = request.forms.get('dateOfBirth')
    composer["dateofdeath"] = request.forms.get('dateOfDeath')
    composer["nationality"] = request.forms.get('nationality')
    composer["style"] = request.forms.get('style')
    print(composer)
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
