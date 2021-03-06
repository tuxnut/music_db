import requests
import datetime
import os
import glob
from BaseDatabase import BaseDatabase

class DatabaseService(BaseDatabase):
    def __init__(self):
        super().__init__()
        self.BASE_URL = "http://" + os.getenv("DB_BASE_URL")
        print("DAS : " + self.BASE_URL)
        self.SCORES_ROUTE = "musicscores"
        self.COMPOSERS_ROUTE = "composers"

    def getAllMusicScores(self, column=''):
        response = requests.get(self.BASE_URL + self.SCORES_ROUTE)
        data = response.json()['musicScores']
        # Adapt date format
        for musicScore in data:
            musicScore['dateofcreation'] = datetime.datetime.strptime(musicScore['dateofcreation'], '%Y-%m-%dT%H:%M:%S.%fZ').year if musicScore['dateofcreation'] is not None else "-"
        return data

    def insertMusicScore(self, musicScore):
        response = requests.post(self.BASE_URL + self.SCORES_ROUTE, json=musicScore)
        
    def updateMusicScore(self, key, musicScore):
        response = requests.put(self.BASE_URL + self.SCORES_ROUTE + "/" + key, json=musicScore)
    
    def deleteMusicScore(self, key):
        response = requests.delete(self.BASE_URL + self.SCORES_ROUTE + "/" + key)

    def getAllComposers(self, column='*'):
        response = requests.get(self.BASE_URL + self.COMPOSERS_ROUTE)
        data = response.json()['composers']
        # Adapt date format
        for composer in data:
            composer['dateofbirth'] = datetime.datetime.strptime(composer['dateofbirth'], '%Y-%m-%dT%H:%M:%S.%fZ').date() if composer['dateofbirth'] is not None else "-"
            composer['dateofdeath'] = datetime.datetime.strptime(composer['dateofdeath'], '%Y-%m-%dT%H:%M:%S.%fZ').date() if composer['dateofdeath'] is not None else "-"
        return data

    def insertComposer(self, composer):
        response = requests.post(self.BASE_URL + self.COMPOSERS_ROUTE, json=composer)

    def updateComposer(self, key, composer):
        response = requests.put(self.BASE_URL + self.COMPOSERS_ROUTE + "/" + key, json=composer)

    def deleteComposer(self, key):
        response = requests.delete(self.BASE_URL + self.COMPOSERS_ROUTE + "/" + key)
        
def retrieveFamilyName(fullName):
    split = fullName.split(' ')
    return split[len(split) - 1]

def computeScorePresence(id, title, composer):
    baseFileName = "%d-%s-%s" % (id, title.replace(' ', '_'), composer.replace(' ', '_'))
    return [file.lstrip('static/sheets/') for file in glob.glob("static/sheets/" + baseFileName + "*")]
