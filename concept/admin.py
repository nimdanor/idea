from django.contrib import admin

from concept.models import Concept,Link


# Permet de définir que Concept est géré dans la zone admin
@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    list_display = ('name', 'lname')

@admin.register(Link)
class LienAdmin(admin.ModelAdmin):
    list_display = ('ascendant','name', 'descendant')


