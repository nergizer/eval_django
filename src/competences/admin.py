from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from competences.models import *

class DefaultAdm(ImportExportModelAdmin):
    pass

class CompetencesAdmin(DefaultAdm):
    pass
# Register your models here.
admin.site.register(UserProfile,DefaultAdm)
admin.site.register(Competence,CompetencesAdmin)
admin.site.register(Requete,DefaultAdm)
