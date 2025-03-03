from django.db import models

# Create your models here.
class Competence(models.Model):
    code = models.CharField(max_length=3)
    definition = models.CharField(max_length=256)

    def __str__(self):
        return self.code + " - " + self.definition
    
    class Meta:
        ordering = ['code']


class PoleActivitesProfessionnelle(models.Model):
    nom = models.CharField(max_length=256)

    def __str__(self):
        return self.nom
    

class ActiviteProfessionnelle(models.Model):
    pole_id = models.ForeignKey(PoleActivitesProfessionnelle, on_delete=models.CASCADE)
    code = models.CharField(max_length=3)
    definition = models.CharField(max_length=256)

    def __str__(self):
        return self.code + " - " + self.definition
    
    class Meta:
        ordering = ['code']


class ActiviteProfessionnelleTache(models.Model):
    activite_professionelle = models.ForeignKey(ActiviteProfessionnelle, on_delete=models.CASCADE)
    code = models.CharField(max_length=3)
    tache = models.CharField(max_length=256)
    autonomie = models.CharField(max_length=64, choices=(("Partielle", "Partielle"), ("Complète", "Complète")), default="Partielle")

    def __str__(self):
        return self.activite_professionelle.code + " - " + self.code + " : " + self.tache
    
    class Meta:
        ordering = ['activite_professionelle', 'code']


class ActiviteProfessionnelleMoyenRessource(models.Model):
    activite_professionelle = models.ForeignKey(ActiviteProfessionnelle, on_delete=models.CASCADE)
    moyen_ressource = models.TextField()

    def __str__(self):
        return self.activite_professionelle.code + " : " + self.moyen_ressource
    
    class Meta:
        ordering = ['activite_professionelle']


class ActiviteProfessionnelleResultat(models.Model):
    activite_professionelle = models.ForeignKey(ActiviteProfessionnelle, on_delete=models.CASCADE)
    resultat = models.TextField()

    def __str__(self):
        return self.activite_professionelle.code + " : " + self.resultat
    
    class Meta:
        ordering = ['activite_professionelle']


class CompetencesByActivitesProfessionnelle(models.Model):
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    activite_professionelle = models.ForeignKey(ActiviteProfessionnelle, on_delete=models.CASCADE)

    def __str__(self):
        return self.competence.code + " - " + self.activite_professionelle.code


class Taxonomie(models.Model):
    niveau = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4)), default=1)
    objectif = models.CharField(max_length=256)
    caracterisation = models.TextField()
    capacite = models.TextField()
    habilete = models.TextField()
    verbe = models.TextField()
    critere_evalusation = models.TextField()
    exemple = models.TextField()

    def __str__(self):
        return "Niveau " + str(self.niveau) + " - " + self.objectif
    
    class Meta:
        ordering = ['niveau']


class ConnaissanceAssociee(models.Model):
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    taxonomie = models.ForeignKey(Taxonomie, on_delete=models.CASCADE)
    connaissance = models.CharField(max_length=256)

    def __str__(self):
        return self.competence.code + " : " + self.connaissance
    

class CompetenceCritereEvaluation(models.Model):
    competence = models.ForeignKey(Competence, on_delete=models.CASCADE)
    critere_evaluation = models.TextField()

    def __str__(self):
        return self.competence.code + " : " + self.critere_evaluation
    

class SequencePedagogique(models.Model):
    nom = models.CharField(max_length=256)
    description = models.TextField()
    objectifs = models.TextField()
    competences = models.ManyToManyField(Competence)
    activites = models.ManyToManyField(ActiviteProfessionnelle)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['nom']


class TypeActivitePedagogique(models.Model):
    nom = models.CharField(max_length=256)
    color = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.nom


class ActivitePedagogique(models.Model):
    sequence_pedagogique = models.ForeignKey(SequencePedagogique, on_delete=models.CASCADE)
    type_activite = models.ForeignKey(TypeActivitePedagogique, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    competence = models.ManyToManyField(Competence)
    activite_professionelle = models.ForeignKey(ActiviteProfessionnelle, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.sequence_pedagogique.nom + " - " + self.activite_professionelle.code
    
    class Meta:
        ordering = ['sequence_pedagogique', 'activite_professionelle']