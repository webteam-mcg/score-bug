import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./lqlk-5370b-firebase-adminsdk-51ysg-0f12a93916.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection(u'main').document(u'live')

doc = doc_ref.get()
data = doc.to_dict()

thisOver = ""
for i in data['thisOver']:
    thisOver = thisOver+i.split(".")[1]+" | "
thisOver = thisOver[:-2]

print('Score\t\t\t', str(data["score"])+"-"+str(data["wickets"]))
print('Overs\t\t\t', (data["balls"]//6)+(data["balls"] % 6)/10)
print('Player 1 Name\t', data['player1']['name'].split(" ")[0])
print('Player 1 Score\t', str(data['player1']['score'])+"("+str(data['player1']['balls'])+")")
print('Player 2 Name\t', data['player2']['name'].split(" ")[0])
print('Player 2 Score\t', str(data['player2']['score'])+"("+str(data['player1']['balls'])+")")
print('Bowler Name\t\t', data['bowler']['name'].split(" ")[0])
print('Bowler Static\t', str(data['bowler']['wickets'])+"-"+str(data['bowler']['score']))
print('This Over\t\t', thisOver)
