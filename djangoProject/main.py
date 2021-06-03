import firebase_admin
import google.cloud.exceptions
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./firebase_credentials.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


def getRoom():
    return {
        "room": "IQFDK",
        "name": "Tim",
        "progression": 80
    }


response = getRoom()
room = response.get('room')
name = response.get('name')
progression = response.get('progression')

doc_ref = db.collection(u'Rooms').document(u'1')
doc_ref.set({
    u'room': room,
    u'name': name,
    u'progression': progression
})
print(room + " and " + name + " succesfully written to database")

try:
    doc = doc_ref.get()
    print(u"Document data: {}".format(doc.to_dict()))
    # do something with data!
except google.cloud.exceptions.NotFound:
    print(u'No such document!')
pass
