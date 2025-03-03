from django.shortcuts import render
from .models import Competence
from .models import ActiviteProfessionnelle
from .models import CompetencesByActivitesProfessionnelle
from .models import ConnaissanceAssociee
from .models import Taxonomie
from .models import CompetenceCritereEvaluation
from .models import ActiviteProfessionnelleTache
from .models import ActiviteProfessionnelleMoyenRessource
from .models import ActiviteProfessionnelleResultat


def index(request):
    competences = Competence.objects.all()
    activite_professionnelles = ActiviteProfessionnelle.objects.all()
    competences_by_activites_professionnelles = CompetencesByActivitesProfessionnelle.objects.all()
    return render(request, 'ciel_referentiel/index.html', {
        "competences": competences, 
        "activites": activite_professionnelles,
        "competences_by_activites_professionnelles" : competences_by_activites_professionnelles})


def detail_competence(request, competence_id):
    competence = Competence.objects.get(pk=competence_id)
    activites = CompetencesByActivitesProfessionnelle.objects.filter(competence=competence)
    connaissances = ConnaissanceAssociee.objects.filter(competence=competence)
    critere_evaluations = CompetenceCritereEvaluation.objects.filter(competence=competence)
    return render(request, 'ciel_referentiel/detail_competence.html',
                  {"competence": competence,
                   "activites": activites,
                   "connaissances": connaissances,
                   "critere_evaluations": critere_evaluations})


def detail_activite_professionnelle(request, activite_id):
    activite = ActiviteProfessionnelle.objects.get(pk=activite_id)
    taches = ActiviteProfessionnelleTache.objects.filter(activite_professionelle=activite)
    moyens_ressources = ActiviteProfessionnelleMoyenRessource.objects.filter(activite_professionelle=activite)
    resultats = ActiviteProfessionnelleResultat.objects.filter(activite_professionelle=activite)
    return render(request, 'ciel_referentiel/detail_activite_professionnelle.html',
                  {"activite": activite,
                   "taches": taches,
                   "moyens_ressources": moyens_ressources,
                   "resultats": resultats})


def detail_taxonomie(request, taxonomie_id):
    taxonomie = Taxonomie.objects.get(pk=taxonomie_id)
    connaissances = ConnaissanceAssociee.objects.filter(taxonomie=taxonomie)
    return render(request, 'ciel_referentiel/detail_taxonomie.html', {"taxonomie": taxonomie, "connaissances": connaissances})