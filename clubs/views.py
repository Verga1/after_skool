from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Club, Category

# Create your views here.

def all_clubs(request):
    """ A view to show all clubs, including sorting and search queries """

    clubs = Club.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                clubs = clubs.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            clubs = clubs.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            clubs = clubs.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('clubs'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            clubs = clubs.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'clubs': clubs,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }    

    return render(request, 'clubs/clubs.html', context)


def club_detail(request, club_id):
    """ A view to show individual club details """

    club = get_object_or_404(Club, pk=club_id)

    context = {
        'club': club,
    }    

    return render(request, 'clubs/club_detail.html', context)