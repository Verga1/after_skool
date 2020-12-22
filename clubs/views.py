from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Club

# Create your views here.

def all_clubs(request):
    """ A view to show all clubs, including sorting and search queries """

    clubs = Club.objects.all()
    query = None

    if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('clubs'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            clubs = clubs.filter(queries)

    context = {
        'clubs': clubs,
        'search_term': query,
    }    

    return render(request, 'clubs/clubs.html', context)


def club_detail(request, club_id):
    """ A view to show individual club details """

    club = get_object_or_404(Club, pk=club_id)

    context = {
        'club': club,
    }    

    return render(request, 'clubs/club_detail.html', context)