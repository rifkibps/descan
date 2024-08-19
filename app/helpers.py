from . import models
from django.db.models import Q
from datetime import date


def count_of_welfare_recips():
    model = models.PopulationsModels.objects.filter(
        Q(family_id__r501a = '1') |
        Q(family_id__r501b = '1') |
        Q(family_id__r501c = '1') |
        Q(family_id__r501d = '1') |
        Q(family_id__r501e = '1') |
        Q(family_id__r501f = '1') |
        Q(family_id__r501g = '1') | 
        Q(r431a = '1')
    ).values('family_id', 'family_id__r108').distinct()

    return model

def labor_participation():
    
    labor_force = models.PopulationsModels.objects.filter(
        Q(r407__gte = 15) & Q(r407__lte = 64) 
    )

    laber_force_work = labor_force.filter(
        (Q(r416a = 1) & ~Q(r416b = 0)) |
        (Q(r420a = 1) & ~Q(r422_23 = 0))
    )

    labor_participation = round(laber_force_work.count() / labor_force.count() * 100, 2)

    return labor_participation

     