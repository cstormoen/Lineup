from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from lineup.models import Lineup, Entry


class OrderedEntryInline(BaseInlineFormSet):
    def get_queryset(self):
        return super(OrderedEntryInline, self).get_queryset().order_by('rank')

class EntryInline(admin.TabularInline):
    model = Entry
    formset = OrderedEntryInline
    extra = 3


class LineupAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'published']
    inlines = [EntryInline]


admin.site.register(Lineup, LineupAdmin)

