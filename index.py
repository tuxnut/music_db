from bottle import Bottle, run, template, debug, request, redirect
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

debug(True)
run(app, host='localhost', port=8080, reloader=True)
