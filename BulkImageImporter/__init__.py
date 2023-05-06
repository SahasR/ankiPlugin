# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *
# file reading abilities
import os

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction() -> None:
    # initializing counter variable
    count = 0
    # fetching the config values
    config = mw.addonManager.getConfig(__name__)

    questionList = []
    answerList = []

    modelBasic = mw.col.models.byName('Basic')
    deck = mw.col.decks.byName(config['deckName'])
    mw.col.decks.select(deck['id'])
    mw.col.decks.current()['mid'] = modelBasic['id']

    folder = QFileDialog.getExistingDirectory(mw, "Import Directory")
    # folder = config['folder']
    questionsDir = os.path.join(folder, 'Questions')
    answersDir = os.path.join(folder, 'Answers')



    for file in os.listdir(questionsDir):
        newPath = os.path.join(folder, questionsDir, file)
        # newPath.replace("\\", '/')
        # Uncomment for Windows :D
        qfile = mw.col.media.addFile(newPath)
        questionList.append(qfile)
        count += 1

    for file in os.listdir(answersDir):
        newPath = os.path.join(folder, answersDir, file)
        # newPath.replace("\\", '/')
        # Uncomment for Windows :D
        afile = mw.col.media.addFile(newPath)
        answerList.append(afile)

    questionList = sorted(questionList)
    answerList = sorted(answerList)

    for x in range(count):
        note = mw.col.newNote()
        note.fields[0] = "<img src='" + str(questionList[x]) + "'>"
        note.fields[1] = "<img src='" + str(answerList[x]) + "'>"
        # note.fields[0] = questionList[x]
        # note.fields[1] = answerList[x]
        mw.col.add_note(note, deck['id'])


    showInfo("Succesfully Added " + str(count) + " cards with images")




# create a new menu item, "test"
action = QAction("Bulk Image Importer.png", mw)
# set it to call testFunction when it's clicked
qconnect(action.triggered, testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)