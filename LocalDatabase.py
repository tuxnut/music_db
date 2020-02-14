import json

class LocalDatabase:
    def __init__(self):
        print("Database is local")
        with open('./mock/localDatabase.json', 'r') as file:
            content = json.load(file)
        self.musicSheetsList = content['musicSheets']
        self.composersList = content['composers']
        self.composerInc = len(self.composersList)

    def getAllMusicSheet(self, column=''):
        return self.musicSheetsList

    def insertMusicSheet(self, musicSheet):
        jsonMusicSheet = {}
        jsonMusicSheet['title'] = musicSheet['title']
        jsonMusicSheet['commonname'] = self.composersList[int(musicSheet['composer'])]['commonname']
        jsonMusicSheet['type'] = musicSheet['type']
        jsonMusicSheet['dateofcreation'] = musicSheet['dateofcreation']
        jsonMusicSheet['difficulty'] = musicSheet['difficulty']
        jsonMusicSheet['appreciation'] = musicSheet['appreciation']
        jsonMusicSheet['comments'] = musicSheet['comments']
        self.musicSheetsList.append(jsonMusicSheet)

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
    print(db.getAllMusicSheet())
    print(db.getAllComposers())