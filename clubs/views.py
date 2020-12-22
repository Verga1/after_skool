from django.shortcuts import render
from .models import Club

# Create your views here.

def all_clubs(request):
    """ A view to show all classes, including sorting and search queries """

    clubs = Club.objects.all()

    context = {
        'clubs': clubs,
    }    

    return render(request, 'clubs/clubs.html', context)