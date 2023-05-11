from django.contrib import admin
from db_demo import models as db_models

# Register your models here.

admin.site.register(db_models.Level0)
admin.site.register(db_models.BridgeGeometry)
admin.site.register(db_models.ProjectDoc)
admin.site.register(db_models.Maintenance)
admin.site.register(db_models.Inspection)
admin.site.register(db_models.Level1)
admin.site.register(db_models.Piece)
#admin.site.register(db_models.FormDefectsAnswer)
admin.site.register(db_models.Defect)

class FormDefectsAnswerInline(admin.TabularInline):
    model = db_models.FormDefectsAnswer
    fields = ('seen', 'defect', 'k1', 'k2', 'note')
    extra=0

@admin.register(db_models.FormDefects)
class FormDefectsAdmin(admin.ModelAdmin):
    inlines = [FormDefectsAnswerInline]


