import sys
import firebase_admin
from firebase_admin import credentials, firestore
import xlsxwriter
import datetime

cred = credentials.Certificate('./lqlk-5370b-firebase-adminsdk-51ysg-0f12a93916.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


doc_ref = db.collection(u'main').document(u'live')

while True:
    doc = doc_ref.get()
    data = doc.to_dict()

    score = str(data["score"])+"-"+str(data["wickets"])
    overs = (data["balls"]//6)+(data["balls"] % 6)/10
    bowlerStatic = str(data['bowler']['wickets'])+"-"+str(data['bowler']['score'])
    player1Name = data['player1']['name'].split(" ")[0]
    player1Score = str(data['player1']['score'])+"("+str(data['player1']['balls'])+")"
    player2Name = data['player2']['name'].split(" ")[0]
    player2Score = str(data['player2']['score']) + "(" + str(data['player1']['balls']) + ")"
    bowlerName = data['bowler']['name'].split(" ")[0]
    thisOver = ""
    for i in data['thisOver']:
        thisOver = thisOver + i.split(".")[1] + " | "
    thisOver = thisOver[:-2]

    workbook = xlsxwriter.Workbook('input.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Text 05')
    worksheet.write('B1', 'Text 11')
    worksheet.write('C1', 'Text 16')
    worksheet.write('D1', 'Text 09')
    worksheet.write('E1', 'Text 14')
    worksheet.write('F1', 'Text 10')
    worksheet.write('G1', 'Text 15')
    worksheet.write('H1', 'Text 13')
    worksheet.write('I1', 'Text 12')

    worksheet.write('A2', score)
    worksheet.write('B2', overs)
    worksheet.write('C2', bowlerStatic)
    worksheet.write('D2', player1Name)
    worksheet.write('E2', player1Score)
    worksheet.write('F2', player2Name)
    worksheet.write('G2', player2Score)
    worksheet.write('H2', bowlerName)
    worksheet.write('I2', thisOver)

    workbook.close()

    print('Last Update:\t' + str(datetime.datetime.now().time()))
