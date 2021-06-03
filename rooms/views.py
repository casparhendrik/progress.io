from django.shortcuts import render

# Create your views here.

def room_view(request):
    databaseCall = 'Tim yhbufgdhbrefh'
    return render(request, 'rooms/main.html', {'T': databaseCall})

