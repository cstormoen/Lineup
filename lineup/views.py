from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponseForbidden
from django.utils import timezone
from django.forms.models import inlineformset_factory
from lineup.models import Lineup, Entry
from lineup.forms import LineupForm, EntryForm, UserForm


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

@login_required
def edit(request, lineup_id):
    try:
        lineup = Lineup.objects.get(pk=lineup_id)
    except Lineup.DoesNotExist:
        raise Http404("Lineup does not exist.")

    EntryFormSet = inlineformset_factory(Lineup, Entry, form=EntryForm)

    if request.method == 'POST':
        lineup_form = LineupForm(request.POST, instance=lineup)
        entry_form_set = EntryFormSet(request.POST, instance=lineup)

        if lineup_form.is_valid() and entry_form_set.is_valid():
            lineup_form.save()
            entry_form_set.save()

        return render(request, 'lineup/view.html', {'lineup': lineup})

    else:
        lineup_form = LineupForm(instance=lineup)
        entry_form_set = EntryFormSet(instance=lineup)

    return render(request, 'lineup/edit.html', {
        'lineup': lineup,
        'lineup_form': lineup_form,
        'entry_form_set': entry_form_set
    })


def new(request):
    if request.method == 'GET':
        lineup_form = LineupForm()

        return render(request, 'lineup/new.html', {
            'lineup_form': lineup_form
        })

    else:
        lineup_form = LineupForm(request.POST)

        if lineup_form.is_valid():
            new_lineup = lineup_form.save(commit=False)
            new_lineup.published = timezone.now()
            new_lineup.author = 'Chris'
            new_lineup.save()

            return redirect('edit', lineup_id=new_lineup.id)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

    else:
        user_form = UserForm()

    return render(request, 'lineup/register.html', {
        'user_form': user_form,
        'registered': registered
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponseForbidden("User no longer active.")
        else:
            return HttpResponseForbidden("Invalid login details.")

    else:
        return render(request, 'lineup/login.html')


@login_required
def user_logout(request):
    logout(request)

    return redirect('index')