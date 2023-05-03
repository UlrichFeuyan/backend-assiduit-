from rest_framework.viewsets import ModelViewSet

from backend.serializers import *


class DepartementViewset(ModelViewSet):
    serializer_class = DepartementSerializer
    queryset = Departement.objects.all()


class FiliereViewset(ModelViewSet):
    serializer_class = FiliereSerializer
    queryset = Filiere.objects.all()


class SpecialiteViewset(ModelViewSet):
    serializer_class = SpecialiteSerializer
    queryset = Specialite.objects.all()


class UtilisateurViewset(ModelViewSet):
    serializer_class = UtilisateurSerializer
    queryset = Utilisateur.objects.all()


class EnseignantViewset(ModelViewSet):
    serializer_class = EnseignantSerializer
    queryset = Enseignant.objects.all()


class ClasseViewset(ModelViewSet):
    serializer_class = ClasseSerializer
    queryset = Classe.objects.all()


class MatiereViewset(ModelViewSet):
    serializer_class = MatiereSerializer
    queryset = Matiere.objects.all()


class CoursViewset(ModelViewSet):
    serializer_class = CoursSerializer
    queryset = Cours.objects.all()


class EtudiantViewset(ModelViewSet):
    serializer_class = EtudiantSerializer
    queryset = Etudiant.objects.all()


class ParentViewset(ModelViewSet):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()


class PresenceViewset(ModelViewSet):
    serializer_class = PresenceSerializer
    queryset = Presence.objects.all()
