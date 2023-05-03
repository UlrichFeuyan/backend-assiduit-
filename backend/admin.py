from django.contrib import admin

from backend.models import *


@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Departement._meta.fields if field.name != 'image'] + ['visuel']
    list_filter = ['nom', 'active']
    list_select_related = True


admin.site.register(Filiere)
admin.site.register(Specialite)
admin.site.register(Utilisateur)
admin.site.register(Enseignant)
admin.site.register(Classe)
admin.site.register(Matiere)
admin.site.register(Cours)
admin.site.register(Etudiant)
admin.site.register(Parent)
admin.site.register(Presence)
