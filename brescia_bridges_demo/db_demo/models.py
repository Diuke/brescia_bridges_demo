from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.gis.db import models as gis_models

# Create your models here.

# Structure type and materials
class StructureType(models.TextChoices):
    ARCO_MURATURA = "ARCOM", _("Arco in Muratura")
    TRAVATE_APPOGGIATE = "TRAVA", _("Travate appoggiate")
    TRAVATE_CONTINUE = "TRAVC", _("Travate continue")
    SOLETTA_CA = "SOLCA", _("Soletta in C.A.")
    SEZIONE_TUBOLARE_CA = "SZTCA", _("Sezione tubolare in c.a.")
    ARCO_CA = "ARCOC", _("Arco in C.A.")
    TRAVATE_GERBER = "TRAVG", _("Travate Gerber")
    CASSONE_PRECOMPRESSO = "CASSP", _("Cassone in Precompresso")
    SEZIONE_TUBOLARE_ACCIAIO = "SZTAC", _("Sezione tubolare in acciaio")
    ARCO_ACCIAIO = "ARCOA", _("Arco in acciaio")
    STRALLATO_O_SOSPESO = "STOSO", _("Strallato o sospeso")
    TRAVATE_CAP_CAVI_POST_TESI = "TRCPT", _("Travate in c.a.p. a cavi post-tesi")
    OTHER = "OTHER", _("Other")

class PresentOptions(models.TextChoices):
    PRESENT = "PR", _("Present")
    ABSENT = "AB", _("Absent")
    NOT_NOTED = "NN", _("Not Noted")
    

class Level0(models.Model):
    #Enums
    class CoordsOptions(models.TextChoices):
        ETRF2000 = "ETRF2000", _("ETRF2000")
        WGS84 = "WGS84", _("WGS84")
    
    class BridgeStatuses(models.TextChoices):
        A = "A", _("Pienamente agibile")
        B = "B", _("Agibile ma con scadenze di lavori di manutenzione straordinaria")
        C = "C", _("Agibile ma con scadenze di lavori di manutenzione straordinaria")
        D = "D", _("Condizioni critiche e agibile parzialmente/lavori di manutenzione urgenti")
        E = "E", _("Inagibile")

    class ConnectionOptions(models.TextChoices):
        WATER_PRINCIPAL = "WATPR", _("Ponte su corso d'acqua del reticolo principale")
        WATER_SECONDARY = "WATSE", _("Ponte su corso d'acqua del reticolo secondario")
        VIADUCT_BUILT = "VIAED", _("Viadotto su zona edificata")
        VIADUCT_ROAD = "VIARO", _("Viadotto su altra via di comunicazione")
        BRIDGE_RAILWAY = "RAILB", _("Ponte su ferrovia")
        BRIDGE_SEA = "RAILS", _("Ponte su specchi d'acqua marini")
        VIADUCT_URB = "VIAUR", _("Viadotto su zona urbanizzata")
        VIADUCT_OROGRAPHY = "VIAOR", _("Ponte/Viadotto su discontinuità orografica (vallata, piccoli canali, ecc.)")

    class RoadClassificationOptions(models.TextChoices):
        TRUNK_RAILWAY = "TRRAIL", _("Autostrada o Ferrovia")
        EXTRAURBAN_PRIMARY = "EXPRIM", _("Strada extraurbana principale")
        EXTRAURBAN_SECONDARY = "EXSECO", _("Strada extraurbana secndaria")
        URBAN_FREEWAY = "URBFREE", _("Strada urbana di scorrimento")
        NEIGHBOURHOOD_ROAD = "NEROAD", _("Strada urbana di quartiere")
        LOCAL_ROAD = "LOROAD", _("Strada locale")

    class MorphologyOptions(models.TextChoices):
        CREST = "CREST", _("Cresta")
        GENTLE_SLOPE = "SLOPE0", _("Pendio dolce (0-10°)")
        MODERATE_SLOPE = "SLOPE1", _("Pendio moderato (10-25°)")
        STEEP_SLOPE = "SLOPE2", _("Pendio ripido (>25°)")
        PLAIN = "PLAIN", _("Pianura")
        PLAIN_SLOPES = "PLAINS", _("Pianura alla base dei versanti")

    class TrackOptions(models.TextChoices):
        RECTILINEAR = "LINE", _("Rettilineo")
        CURVE = "CURVE", _("In curva")

    class PileMaterialOptions(models.TextChoices):
        MASONRY = "MA", _("Muratura")
        CA = "CA", _("C.A.")
        CAP = "CAP", _("C.A.P.")
        STEEL = "ACC", _("Acciaio")
        MIXED = "MX", _("Misto (C.A./Acciaio)")
        WOOD = "LEG", _("Legno")
        OTHER = "OTHER", _("Other")

    class SlabMaterialOptions(models.TextChoices):
        CA = "CA", _("C.A.")
        CAP = "CAP", _("C.A.P.")
        STEEL = "ACC", _("Acciaio")
        MIXED = "MX", _("Misto (C.A./Acciaio)")
        WOOD = "LEG", _("Legno")
        OTHER = "OTHER", _("Other")

    #main information
    iop_code = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=255, default="")
    street = models.CharField(max_length=255, default="")
    initial_km = models.CharField(max_length=50, default="")
    final_km = models.CharField(max_length=50, default="")

    #location information
    prov_region = models.CharField(max_length=255, default="Brescia/Lombardia")
    municipality = models.CharField(max_length=255, default="")
    locality = models.CharField(max_length=255, default="")
    seismicity = models.FloatField(max_length=10, default="")

    #coordinates type
    coord_geo_type = models.CharField(
        choices= CoordsOptions.choices,
        default= CoordsOptions.WGS84,
        verbose_name="Coordinates type"
    )
    #center coordinates
    center_elevation = models.FloatField(max_length=20, default="")
    center_longitude = models.FloatField(max_length=20, default="")
    center_latitude = models.FloatField(max_length=20, default="")
    #starting coordinates
    initial_elevation = models.FloatField(max_length=20, default="")
    initial_longitude = models.FloatField(max_length=20, default="")
    initial_latitude = models.FloatField(max_length=20, default="")
    #ending coordinates
    final_elevation = models.FloatField(max_length=20, default="")
    final_longitude = models.FloatField(max_length=20, default="")
    final_latitude = models.FloatField(max_length=20, default="")

    #erosion and flooding events
    erosion_flooding_events = models.CharField(
        choices=PresentOptions.choices,
        max_length=2,
        default=PresentOptions.NOT_NOTED,
    )
    #landslides events
    landslide_events = models.CharField(
        choices=PresentOptions.choices,
        max_length=2,
        default=PresentOptions.NOT_NOTED,
    )

    #general information
    propietary = models.CharField(max_length=255, default="")
    concessionary = models.CharField(max_length=255, default="")
    vigilant_body = models.CharField(max_length=255, default="")

    #project year [...]

    #legislation
    safeguard_measures = models.CharField(max_length=255, default="")
    project_author = models.CharField(max_length=255, default="")
    landscape_plans = models.CharField(max_length=255, default="", verbose_name="Inclusion of the bridge in existing/adopted Landscape Plans")

    #bridge status
    bridge_status = models.CharField(
        choices=BridgeStatuses.choices,
        max_length=1,
        null=True
    )

    #link classification and road use classification
    connection_type = models.CharField(
        choices=ConnectionOptions.choices,
        max_length=5,
        null=True
    )
    road_type = models.CharField(
        choices=RoadClassificationOptions.choices,
        max_length=7,
        null=True
    )

    #geomorphological data
    site_morphology = models.CharField(
        choices=MorphologyOptions.choices,
        max_length=6,
    )

    #bridge geometry
    extended_light = models.FloatField(max_length=10, verbose_name="Extended overall light [m]")
    total_deck_width = models.FloatField(max_length=10, verbose_name="Total deck width [m]")
    spans_number = models.IntegerField()
    spans_light = models.FloatField(max_length=10)
    track_type = models.CharField(
        choices=TrackOptions.choices,
        max_length=5
    )

    #structural typology
    bridge_type = models.CharField(
        choices=StructureType.choices,
        max_length=5,
        default=StructureType.OTHER,
    )
    bridge_type_other = models.CharField(max_length=255, null=True, blank=True, default=None, verbose_name="Altro")

    #aboutments
    initial_aboutment_type = models.CharField(max_length=255, default="")
    initial_aboutment_foundations = models.CharField(max_length=255, default="")
    final_aboutment_type = models.CharField(max_length=255, default="")
    final_aboutment_foundations = models.CharField(max_length=255, default="")

    #piles
    piles_material = models.CharField(
        choices=PileMaterialOptions.choices,
        max_length=5,
        default=PileMaterialOptions.OTHER,
    )
    piles_material_other = models.CharField(max_length=255, null=True, blank=True, default=None, verbose_name="Altro")

    cross_section_type = models.CharField(max_length=255, default="")
    foundations_type = models.CharField(max_length=255, default="")
    piles_height = models.IntegerField(max_length="2", verbose_name="Piles height [m]")
    cross_section_geometry = models.CharField(max_length=50, default="")
    foundations_number = models.IntegerField(max_length=2)
    riverbed_evolution = models.CharField(max_length=255, default="", verbose_name="Possible evolution with respect to the river bed")

    #deck
    deck_material = models.CharField(
        choices=PileMaterialOptions.choices,
        max_length=5,
        default=PileMaterialOptions.OTHER,
    )
    deck_material_other = models.CharField(max_length=255, null=True, blank=True, default=None, verbose_name="Altro")
    slab_material = models.CharField(
        choices=SlabMaterialOptions.choices,
        max_length=5,
        default=SlabMaterialOptions.OTHER,
    )
    slab_material_other = models.CharField(max_length=255, null=True, blank=True, default=None, verbose_name="Altro")

    #Protection systems and support equipment
    protection_systems_type = models.CharField(max_length=100, default="")
    support_equipment_type = models.CharField(max_length=100, default="")
    track_width = models.FloatField(max_length=6, verbose_name="Track width [m]")
    antiseimic_equipment_type = models.CharField(max_length=255, default="")

    #joints
    joints_type = models.CharField(max_length=255, default="")
    aboutment_joint_distance = models.FloatField(max_length=10, default="")
    total_joints_number = models.IntegerField()
    pile_joint_distance = models.FloatField(max_length=10, default="")

    #description of structural interventions executed
    masonry_vault = models.BooleanField(max_length=1,default="")
    masonry_vault_description = models.CharField(max_length=255, default="")
    structural_elements_repair_or_replacement = models.BooleanField(max_length=1, default="")
    structural_elements_repair_or_replacement_description = models.CharField(max_length=255, default="")
    roadway_widening = models.BooleanField(max_length=1,default="")
    roadway_widening_description = models.CharField(max_length=255, default="")
    additional_structural_elements = models.BooleanField(max_length=1,default="")
    additional_structural_elements_description = models.CharField(max_length=255, default="")
    geotechnical_interventions = models.BooleanField(max_length=1,default="")
    geotechnical_interventions_description = models.CharField(max_length=255, default="")
    mitigation_interventions = models.BooleanField(max_length=1,default="")
    mitigation_interventions_description = models.CharField(max_length=255, default="")
    other_interventions_description = models.CharField(max_length=255, default="")

    #maintenance
    maintenance_present = models.CharField(
        choices=PresentOptions.choices,
        max_length=2,
        default=PresentOptions.NOT_NOTED,
    )
    #number of maintenance operations should be a calculated field
    #last maintenance date should be a calculated field


    maintenance_plan = models.CharField(max_length=255, default="")


    #inspections
    inspections_present = models.CharField(
        choices=PresentOptions.choices,
        max_length=2,
        default=PresentOptions.NOT_NOTED,
    )
    #number of inspections should be a calculated field
    #last inspection date should be a calculated field
    significant_results = models.CharField(max_length=255, default="")

    past_monitoring_activities = models.CharField(
        choices=PresentOptions.choices,
        max_length=2,
        default=PresentOptions.NOT_NOTED,
    )
    survey_type = models.CharField(max_length=255, default="")
    monitoring_methodology = models.CharField(max_length=255, default="")
    starting_date = models.DateField(default="")
    last_update_date = models.DateField(default="")
    finishing_date = models.DateField(default="")
    equipment_type = models.CharField(max_length=255, default="")
    measured_variables = models.CharField(max_length=255, default="")
    significant_results = models.CharField(max_length=255, default="")
    alert_level = models.CharField(max_length=255, default="")
    related_documentation = models.CharField(max_length=255, default="")
    attachment_n = models.CharField(max_length=10, default="")

    #road network
    

    ### ADD MORE ###

    def __str__(self):
        return f"Bridge {self.iop_code} - {self.name}"

    class Meta:
        db_table = "level_0"
        verbose_name_plural = "Bridges Level 0 information" 
        verbose_name = "Bridge Level 0 information"

class BridgeGeometry(models.Model):
    #change for a real geometry representation
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    geometry_points = gis_models.PointField(null=True, srid=3857)

    level_0 = models.OneToOneField(
        "Level0",
        on_delete=models.CASCADE,
        blank=True,
        default=None, 
        related_name="level_0_geometry"
    )

    def __str__(self):
        if self.level_0:
            return f"Bridge {self.level_0.iop_code} - {self.level_0.name}"
        else:
            return f"Bridge without data"

    class Meta:
        db_table = "bridge_geometry"
        verbose_name_plural = "Bridges Geometries"
        verbose_name = "Bridge Geometry"

class ProjectDoc(models.Model):
    #Add a real document (file) field here
    name = models.CharField(max_length=255, default="")

    level_0 = models.ForeignKey(
        "Level0",
        on_delete=models.CASCADE,
        blank=True,
        default=None
    )

    class Meta:
        db_table = "project_doc"
        verbose_name_plural = "Project Documents"
        verbose_name = "Project Document"

class Maintenance(models.Model):
    date = models.DateField(default="")
    maintenance_type = models.CharField(max_length=255, default="")
    documentation = models.CharField(max_length=255, default="") #make this a document!

    level_0 = models.ForeignKey(
        "Level0",
        on_delete=models.CASCADE,
        blank=True,
        default=None
    )

    class Meta:
        db_table = "maintenance"
        verbose_name_plural = "Maintenance entries"
        verbose_name = "Maintenance"

class Inspection(models.Model):
    date = models.DateField()
    methodology = models.CharField(max_length=255, default="")
    inspection_body = models.CharField(max_length=255)
    documentation = models.CharField(max_length=255) #make this a document!

    level_0 = models.ForeignKey(
        "Level0",
        on_delete=models.CASCADE,
        blank=True,
        default=None
    )

    class Meta:
        db_table = "inspection"
        verbose_name_plural = "Inspections"
        verbose_name = "Inspection"

class Level1(models.Model):
    #enums
    

    street = models.CharField(max_length=255,default="")
    km = models.CharField(max_length=255,default="")
    tecnico = models.CharField(max_length=255,default="")
    inspection_date = models.DateField(default="")

    structure_type = models.CharField(
        choices=StructureType.choices,
        max_length=5,
        default=StructureType.OTHER,
    )
    structure_type_other = models.CharField(max_length=255, null=True, blank=True, default=None)


    #Should be related to one inspection
    inspection = models.OneToOneField(
        "Inspection",
        on_delete=models.CASCADE,
        blank=True,
        default=None,
        related_name="inspection_level_1"
    )
    class Meta:
        db_table = "level_1"
        verbose_name_plural = "Inspections Level 1 information"
        verbose_name = "Inspection Level 1 information"

class FormDefects(models.Model):
    piece_number = models.IntegerField(default=1)
    notes = models.TextField(default="", blank=True)
    
    level_1 = models.ForeignKey(
        "Level1",
        on_delete=models.CASCADE,
        blank=True,
        default=None
    )

    piece = models.ForeignKey(
        "Piece",
        on_delete=models.PROTECT,
        blank=True,
        default=None
    )

    class Meta:
        db_table = "form_defects"
        verbose_name_plural = "Forms of Defects"
        verbose_name = "Form of Defects"
        unique_together = ('piece', 'piece_number', 'level_1') #no same piece and piece number for the same level 1 inspection


class Piece(models.Model):
    id = models.IntegerField(primary_key=True)
    structural_element = models.CharField(max_length=255, default="")
    material = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return str(self.id) + ", " + str(self.structural_element) + ", " + str(self.material)

    class Meta:
        db_table = "piece"
        verbose_name_plural = "Pieces"
        verbose_name = "Piece"

class FormDefectsAnswer(models.Model):
    #enums
    class K1_Options(models.TextChoices):
        ZEROTWO = "0,2", _("0,2")
        ZEROFIVE = "0,5", _("0,5")
        ONE = "1", _("1")
        NONE = None, _("Empty")

    class K2_Options(models.TextChoices):
        ZEROTWO = "0,2", _("0,2")
        ZEROFIVE = "0,5", _("0,5")
        ONE = "1", _("1")
        NONE = None, _("Empty")

    class IncompleteReasons(models.TextChoices):
        NA = "NA", _("Non Applicabile")
        NR = "NR", _("Non Rilevabile")
        NP = "NP", _("Non Present")
        NONE = None, _("Empty")

    class PSOptions(models.TextChoices):
        YES = "YES", _("YES")
        NO = "NO", _("NO")
        NA = None, _("Non Applica") 

    #fields
    seen = models.BooleanField(default=False, verbose_name="Visto")
    k1 = models.CharField(
        choices=K1_Options.choices,
        max_length=10,
        null=True, 
        default=K1_Options.NONE,
        verbose_name="Estensione K1"
    )

    k2 = models.CharField(
        choices=K2_Options.choices,
        max_length=10,
        null=True,
        default=K1_Options.NONE,
        verbose_name="Intensità K2"
    )

    n_photo = models.CharField(max_length=255, default="", null=True, blank=True)

    ps = models.CharField(
        choices=PSOptions.choices, 
        max_length=10,
        null=True,
        default=PSOptions.NA,
        verbose_name='Pregiudica Statica (PS)'
    )

    incomplete_reason = models.CharField(
        choices=IncompleteReasons.choices, 
        max_length=10,
        null=True, 
        default=None,
    )
    note = models.TextField(default="", blank=True) 

    form_defects = models.ForeignKey(
        "FormDefects", 
        on_delete=models.CASCADE,
        blank=True, 
        default=None 
    )

    defect = models.OneToOneField(
        "Defect",
        primary_key=True,
        on_delete=models.CASCADE,
        blank=True,
        default=None
    )

    def defect_g(self):
        return self.defect.g
    defect_g.short_description = u'G'
    
    class Meta:
        db_table = "form_defects_answer"
        verbose_name_plural = "Answers of Form of Defects"
        verbose_name = "Answers of Form of Defects"
        unique_together = ('defect', 'form_defects')

class Defect(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=255, default="")
    g = models.IntegerField(
        default=1, 
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    piece = models.ManyToManyField(Piece)

    def __str__(self):
        return str(self.code) + " - " + str(self.description)

    class Meta:
        db_table = "defect"
        verbose_name_plural = "Defects"
        verbose_name = "Defect"