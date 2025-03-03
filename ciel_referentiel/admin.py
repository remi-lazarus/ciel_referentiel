from django.contrib import admin

# Register your models here.
from .models import Competence
from .models import CompetencesByActivitesProfessionnelle
from .models import PoleActivitesProfessionnelle
from .models import ActiviteProfessionnelle
from .models import Taxonomie
from .models import ConnaissanceAssociee
from .models import CompetenceCritereEvaluation
from .models import ActiviteProfessionnelleTache
from .models import ActiviteProfessionnelleMoyenRessource
from .models import ActiviteProfessionnelleResultat
from .models import TypeActivitePedagogique
from .models import ActivitePedagogique
from .models import SequencePedagogique

admin.site.register(PoleActivitesProfessionnelle)
admin.site.register(Competence)
admin.site.register(ActiviteProfessionnelle)
admin.site.register(CompetencesByActivitesProfessionnelle)
admin.site.register(Taxonomie)
admin.site.register(ConnaissanceAssociee)
admin.site.register(CompetenceCritereEvaluation)
admin.site.register(ActiviteProfessionnelleTache)
admin.site.register(ActiviteProfessionnelleMoyenRessource)
admin.site.register(ActiviteProfessionnelleResultat)
admin.site.register(TypeActivitePedagogique)
admin.site.register(ActivitePedagogique)
admin.site.register(SequencePedagogique)