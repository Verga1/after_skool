from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from clubs.models import Club


def bag_contents(request):

    bag_items = []
    total = 0
    club_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        club = get_object_or_404(Club, pk=item_id)
        total += quantity * club.price
        club_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'club': club,
        })

    if club_count >= settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE / 100)
        discount_delta = 0
    else:
        discount = 0
        discount_delta = club_count + 1

    grand_total = total - discount

    request.session['club_count'] = club_count

    context = {
        'bag_items': bag_items,
        'total': total,
        'club_count': club_count,
        'discount': discount,
        'discount_delta': discount_delta,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
