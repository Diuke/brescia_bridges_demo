from django.contrib import admin
from django.contrib.gis.forms.widgets import OSMWidget
from db_demo import models as db_models
from django.contrib.gis.db.models import MultiPointField, PointField

# Register your models here.

class CustomOSMWidget(OSMWidget):
    """
    An OpenLayers/OpenStreetMap-based widget.
    """

    template_name = "admin/gis/custom-gis-openlayers-osm.html"  
 
    def __init__(self, attrs=None):
        default_lon = 10.2288 
        default_lat = 45.5384
        default_zoom = 10 

        super().__init__()  
        self.attrs['default_lon'] = default_lon 
        self.attrs['default_lat'] = default_lat 
        self.attrs['default_zoom'] = default_zoom  

class BridgeGeometryInline(admin.StackedInline):
    model = db_models.BridgeGeometry

    formfield_overrides = {
        MultiPointField: {
            "widget": CustomOSMWidget 
        },
        PointField: {   
            "widget": CustomOSMWidget
        },
    }


class InspectionInline(admin.StackedInline):
    model = db_models.Inspection
    extra=0
    fields=["date", "methodology", "inspection_body", "documentation"]

class MaintenanceInline(admin.StackedInline):
    model = db_models.Maintenance
    extra=0

class ProjectDocInline(admin.StackedInline):
    model = db_models.ProjectDoc
    extra=0

@admin.register(db_models.Level0)
class Level0Admin(admin.ModelAdmin):
    inlines = [BridgeGeometryInline, InspectionInline, MaintenanceInline, ProjectDocInline]

admin.site.register(db_models.Level1)

@admin.register(db_models.Piece)
class PieceAdmin(admin.ModelAdmin):
    ordering = ['id']

@admin.register(db_models.Defect)
class DefectAdmin(admin.ModelAdmin):
    ordering = ['code']
    search_fields = ['code', 'description']

#Form defects
class FormDefectsAnswerInline(admin.TabularInline): 
    model = db_models.FormDefectsAnswer
    template = "admin/edit_inline/custom-tabular.html"
    fieldsets = [
        ('Visto', {'fields': ['seen']}),
        ('Difetti', {'fields': ['defect', 'defect_g']}),
        ('Dati', {'fields': ['k1', 'k2', 'incomplete_reason', 'n_photo', 'ps', 'note']})
    ]
    readonly_fields = ['defect_g']
    extra=0
    can_delete=False

    def has_add_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(db_models.FormDefects)
class FormDefectsAdmin(admin.ModelAdmin):
    inlines = [FormDefectsAnswerInline]

    class Media:
        js = ['js/form_defects.js']
        css = {
            "all": ['css/form_defects.css'],
        }

    def get_form(self, request, obj=None, **kwargs):
        form = super(FormDefectsAdmin, self).get_form(request, obj, **kwargs)
        #Dont allow to modify or add new Level 1 or Piece elements
        field = form.base_fields["level_1"] 
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field.widget.can_view_related = False
        field.widget.can_delete_related = False
        field = form.base_fields["piece"]
        field.widget.can_add_related = False
        field.widget.can_change_related = False
        field.widget.can_view_related = False
        field.widget.can_delete_related = False
        return form
    
    