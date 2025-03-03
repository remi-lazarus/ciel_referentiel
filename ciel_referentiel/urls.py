from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("competence/<int:competence_id>/", views.detail_competence, name="detail_competence"),
    path("activite/<int:activite_id>/", views.detail_activite_professionnelle, name="detail_activite_professionnelle"),
    path("taxonomie/<int:taxonomie_id>/", views.detail_taxonomie, name="detail_taxonomie"),
    #path("add_sequence/", views.add_sequence, name="add_sequence"),
    #path("add_activite/", views.add_activite, name="add_activite"),
]