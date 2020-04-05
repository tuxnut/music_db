import json

class LocalDatabase:
    def __init__(self):
        print("Database is local")
        with open('../mock/localDatabase.json', 'r') as file:
            content = json.load(file)
        self.musicScoreList = content['musicScores']
        self.composersList = content['composers']
        self.composerInc = len(self.composersList)

    def getAllMusicScores(self, column=''):
        return self.musicScoreList

    def insertMusicScore(self, musicScore):
        jsonMusicScore = {}
        jsonMusicScore['title'] = musicScore['title']
        jsonMusicScore['commonname'] = self.composersList[int(musicScore['composer'])]['commonname']
        jsonMusicScore['type'] = musicScore['type']
        jsonMusicScore['dateofcreation'] = musicScore['dateofcreation']
        jsonMusicScore['difficulty'] = musicScore['difficulty']
        jsonMusicScore['appreciation'] = musicScore['appreciation']
        jsonMusicScore['comments'] = musicScore['comments']
        self.musicScoreList.append(jsonMusicScore)

    def getAllComposers(self, column='*'):
        return self.composersList

    def insertComposer(self, composer):
        jsonComposer = {}
        jsonComposer['commonname'] = composer['name']
        jsonComposer['fullname'] = composer['fullname']
        jsonComposer['dateofbirth'] = composer['dateofbirth']
        jsonComposer['dateofdeath'] = composer['dateofdeath']
        jsonComposer['nationality'] = composer['nationality']
        jsonComposer['style'] = composer['style']
        jsonComposer['composer_id'] = self.composerInc
        self.composerInc += 1
        self.composersList.append(jsonComposer)

if __name__ == "__main__":
    db = LocalDatabase()
    print(db.getAllMusicScore())
    print(db.getAllComposers())