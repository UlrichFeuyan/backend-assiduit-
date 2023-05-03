import os

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe

SEXE_CHOICES = [
    ('masculin', 'Masculin'),
    ('feminin', 'Féminin'),
]


def img_path(instance, filename):
    path = f"backend/{type(instance).__name__}/"
    ext = filename.split('.')[-1]
    return os.path.join(path, filename)


class Departement(models.Model):
    image = models.ImageField("Image - Departement", upload_to=img_path, blank=True, null=True)
    nom = models.CharField(max_length=255)
    description = RichTextField(verbose_name="Description", blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Département"
        verbose_name_plural = "Départements"

    def __str__(self):
        return self.nom

    @property
    def description_text(self):
        return strip_tags(self.description)

    def visuel(self):
        return mark_safe(
            '<img src="{}" alt="{}" width="100" />'.format(self.image.url, self.__str__()))

    visuel.allow_tags = True


class Filiere(models.Model):
    image = models.ImageField("Image - Filiere", upload_to=img_path, blank=True, null=True)
    nom = models.CharField(max_length=255)
    description = RichTextField(verbose_name="Description", blank=True, null=True)
    departement = models.ForeignKey(Departement, verbose_name="Département", on_delete=models.DO_NOTHING)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Filière"
        verbose_name_plural = "Filières"

    def __str__(self):
        return self.nom

    @property
    def description_text(self):
        return strip_tags(self.description)

    def visuel(self):
        return mark_safe(
            '<img src="{}" alt="{}" width="100" />'.format(self.image.url, self.__str__()))

    visuel.allow_tags = True


class Specialite(models.Model):
    image = models.ImageField("Image - Specialite", upload_to=img_path, blank=True, null=True)
    nom = models.CharField(max_length=255)
    description = RichTextField(verbose_name="Description", blank=True, null=True)
    filiere = models.ForeignKey(Filiere, verbose_name="Filière", on_delete=models.DO_NOTHING)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Spécialite"
        verbose_name_plural = "Spécialites"

    def __str__(self):
        return self.nom

    @property
    def description_text(self):
        return strip_tags(self.description)

    def visuel(self):
        return mark_safe(
            '<img src="{}" alt="{}" width="100" />'.format(self.image.url, self.__str__()))

    visuel.allow_tags = True


class Utilisateur(models.Model):
    image = models.ImageField("Image - Utilisateur", upload_to=img_path, blank=True, null=True)
    nom = models.CharField(max_length=255)
    sexe = models.CharField(max_length=15, choices=SEXE_CHOICES, null=True)
    telephone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_naissance = models.DateField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.nom

    def visuel(self):
        return mark_safe(
            '<img src="{}" alt="{}" width="100" />'.format(self.image.url, self.__str__()))

    visuel.allow_tags = True


class Enseignant(Utilisateur):
    matricule = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"

    def __str__(self):
        return self.nom

    def visuel(self):
        return mark_safe(
            '<img src="{}" alt="{}" width="100" />'.format(self.image.url, self.__str__()))

    visuel.allow_tags = True


class Classe(models.Model):
    image = models.ImageField("Image - Classe", upload_to=img_path, blank=True, null=True)
    nom = models.CharField(max_length=50)
    label = models.CharField(max_length=25)
    niveau = models.IntegerField()

    specialite = models.ForeignKey(Specialite, verbose_name="Spécialite", on_delete=models.DO_NOTHING)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Classe"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.nom

    def visuel(self):
        return mark_safe(
            '<img src="{}" alt="{}" width="100" />'.format(self.image.url, self.__str__()))

    visuel.allow_tags = True


class Matiere(models.Model):
    image = models.ImageField("Image - Matiere", upload_to=img_path, blank=True, null=True)
    nom = models.CharField(max_length=255)
    semestre = models.IntegerField()

    enseignant = models.ForeignKey(Enseignant, verbose_name="Enseignant", on_delete=models.DO_NOTHING)
    classe = models.ManyToManyField(Classe, verbose_name="Classe", related_name="Classe", related_query_name='matiere',
                                    blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Matière"
        verbose_name_plural = "Matières"

    def __str__(self):
        return self.nom

    def visuel(self):
        return mark_safe(
            '<img src="{}" alt="{}" width="100" />'.format(self.image.url, self.__str__()))

    visuel.allow_tags = True


class Cours(models.Model):
    image = models.ImageField("Image - Cours", upload_to=img_path, blank=True, null=True)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    matiere = models.ForeignKey(Matiere, verbose_name="Matière", on_delete=models.DO_NOTHING)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Cours"
        verbose_name_plural = "Cours"

    def __str__(self):
        return f"{self.matiere.nom}({self.date} : {self.heure_debut} - {self.heure_fin})"

    def visuel(self):
        return mark_safe(
            '<img src="{}" alt="{}" width="100" />'.format(self.image.url, self.__str__()))

    visuel.allow_tags = True


class Etudiant(Utilisateur):
    matricule = models.CharField(max_length=100)
    Classe = models.ForeignKey(Classe, verbose_name="Classe", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Étudiant"
        verbose_name_plural = "Étudiants"

    def __str__(self):
        return self.nom

    def visuel(self):
        return mark_safe(
            '<img src="{}" alt="{}" width="100" />'.format(self.image.url, self.__str__()))

    visuel.allow_tags = True


class Parent(Utilisateur):
    etudiant = models.ManyToManyField(Etudiant, verbose_name="Étudiant", related_name="Étudiant",
                                      related_query_name='etudiants', blank=True)

    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

    def __str__(self):
        return self.nom

    def visuel(self):
        return mark_safe(
            '<img src="{}" alt="{}" width="100" />'.format(self.image.url, self.__str__()))

    visuel.allow_tags = True


class Presence(models.Model):
    image = models.ImageField("Image - Presence", upload_to=img_path, blank=True, null=True)
    presence = models.BooleanField()
    retard = models.BooleanField()
    demission = models.BooleanField()

    etudiant = models.ForeignKey(Etudiant, verbose_name="Étudiant", on_delete=models.DO_NOTHING)
    cours = models.ForeignKey(Cours, verbose_name="Cours", on_delete=models.DO_NOTHING)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Présence"
        verbose_name_plural = "Présences"

    def __str__(self):
        if self.presence:
            return f"{self.etudiant.nom} : Présent"
        return f"{self.etudiant.nom} : Absent"

    def visuel(self):
        return mark_safe(
            '<img src="{}" alt="{}" width="100" />'.format(self.image.url, self.__str__()))

    visuel.allow_tags = True
