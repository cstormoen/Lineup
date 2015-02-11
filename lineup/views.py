from django.shortcuts import render
from django.http import Http404
from django.forms.models import inlineformset_factory
from lineup.models import Lineup, Entry
from lineup.forms import LineupForm, EntryForm


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

    EntryFormSet = inlineformset_factory(Lineup, Entry, form=EntryForm)

    if request.method == 'POST':
        lineup_form = LineupForm(request.POST, instance=lineup)
        entry_form_set = EntryFormSet(request.POST, instance=lineup)

        if lineup_form.is_valid():
            lineup_form.save()

        if entry_form_set.is_valid():
            entry_form_set.save()

        return render(request, 'lineup/view.html', {'lineup': lineup})

    else:
        lineup_form = LineupForm(instance=lineup)
        entry_form_set = EntryFormSet(instance=lineup)

    return render(request, 'lineup/edit.html',
                  {'lineup': lineup,
                   'lineup_form': lineup_form,
                   'entry_form_set': entry_form_set})