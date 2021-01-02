from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Club, Category
from .forms import ClubForm

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
            if sortkey == 'category':
                sortkey = 'category__name'

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


@login_required
def add_club(request):
    """ Add a club to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            club = form.save()
            messages.success(request, 'Successfully added club!')
            return redirect(reverse('club_detail', args=[club.id]))
        else:
            messages.error(request, 'Failed to add club. Please ensure the form is valid.')
    else:
        form = ClubForm()

    template = 'clubs/add_club.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_club(request, club_id):
    """ Edit a club in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only owners can do that.')
        return redirect(reverse('home'))

    club = get_object_or_404(Club, pk=club_id)
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES, instance=club)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated club!')
            return redirect(reverse('club_detail', args=[club.id]))
        else:
            messages.error(request, 'Failed to update club. Please ensure the form is valid.')
    else:
        form = ClubForm(instance=club)
        messages.info(request, f'You are editing {club.name}')

    template = 'clubs/edit_club.html'
    context = {
        'form': form,
        'club': club,
    }

    return render(request, template, context)


@login_required
def delete_club(request, club_id):
    """ Delete a club from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only owners can do that.')
        return redirect(reverse('home'))

    club = get_object_or_404(Club, pk=club_id)
    club.delete()
    messages.success(request, 'Club deleted!')
    return redirect(reverse('clubs'))