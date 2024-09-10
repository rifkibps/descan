from django.contrib import admin
from . import models
# Register your models here.


class PopulationsStacked(admin.StackedInline):
    model = models.PopulationsModels

class FamiliesItems(admin.ModelAdmin):
    inlines = [PopulationsStacked]

admin.site.register(models.OfficerModels)
admin.site.register(models.RegionAdministrativeModels)
admin.site.register(models.RegionSLSModels)
admin.site.register(models.FamiliesModels, FamiliesItems)

