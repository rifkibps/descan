from django.contrib import admin
from . import models
# Register your models here.


class CharacteristicItemsStacked(admin.StackedInline):
    model = models.BackendCharacteristicItemsModel

class CharacteristicItems(admin.ModelAdmin):
    inlines = [CharacteristicItemsStacked]

admin.site.register(models.RegionAdministrativeModels)
admin.site.register(models.RegionSLSModels)
admin.site.register(models.FamiliesModels)