from django.shortcuts import render
from lineup.models import Lineup


def index(request):
    lineup_list = Lineup.objects.order_by('published')
    context = {
        'lineup_list': lineup_list
    }
    return render(request, 'lineup/index.html', context)
