from django.shortcuts import render
from django.http import Http404
from lineup.models import Lineup


def index(request):
    lineup_list = Lineup.objects.order_by('published')
    context = {
        'lineup_list': lineup_list
    }
    return render(request, 'lineup/index.html', context)


def view(request, lineup_id):
    try:
        lineup = Lineup.objects.get(pk=lineup_id)
    except Lineup.DoesNotExist:
        raise Http404("Lineup does not exist.")

    return render(request, 'lineup/view.html', {'lineup': lineup})


def edit(request, lineup_id):
    try:
        lineup = Lineup.objects.get(pk=lineup_id)
    except Lineup.DoesNotExist:
        raise Http404("Lineup does not exist.")

    return render(request, 'lineup/edit.html', {'lineup': lineup})