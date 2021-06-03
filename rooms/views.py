from django.shortcuts import render

from rooms.models import Room
import firebase_admin
import google.cloud.exceptions
from firebase_admin import credentials, firestore

cred = credentials.Certificate('')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

# Create your views here.

def room_view(request):
    room = request.POST.get('room', '')
    print(room)
    if room != '':
        room = get_room(room)
        databaseCall = room
        return render(request, 'rooms/main.html', {'T': databaseCall})
    else:
        databaseCall = 'No room selected'
        return render(request, 'rooms/main.html', {'T': databaseCall})

def get_room(room):
    rooms_ref = db.collection(u'Rooms')
    rooms = rooms_ref.where(u'room', u'==', room).get()

    # loops through all rooms, count of rooms should be one since each room is unique.
    roomObj = {

    }
    for room in rooms:
        roomObj = Room(**room.to_dict())

    return roomObj
