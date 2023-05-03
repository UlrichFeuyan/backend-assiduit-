from django.urls import path, include
from rest_framework import routers

from .views import *
router = routers.SimpleRouter()
router.register('departement', DepartementViewset, basename='departement')
router.register('filiere', FiliereViewset, basename='filiere')
router.register('specialite', SpecialiteViewset, basename='specialite')
router.register('utilisateur', UtilisateurViewset, basename='utilisateur')
router.register('enseignant', EnseignantViewset, basename='enseignant')
router.register('classe', ClasseViewset, basename='classe')
router.register('matiere', MatiereViewset, basename='matiere')
router.register('cours', CoursViewset, basename='cours')
router.register('etudiant', EtudiantViewset, basename='etudiant')
router.register('parent', ParentViewset, basename='parent')
router.register('presence', PresenceViewset, basename='presence')

app_name = 'backend'
urlpatterns = [
    path('', include(router.urls)),
]