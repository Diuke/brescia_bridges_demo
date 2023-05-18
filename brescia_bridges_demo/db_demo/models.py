from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Level0(models.Model):
    #Enums
    class PresentOptions(models.TextChoices):
        PRESENT = "PR", _("Present")
        ABSENT = "AB", _("Absent")
        NOT_NOTED = "NN", _("Not Noted")

    #main information
    iop_code = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=255, default="")
    street = models.CharField(max_length=255, default="")
    initial_km = models.CharField(max_length=50, default="")
    final_km = models.CharField(max_length=50, default="")

    #location information

    #general information
    propietary = models.CharField(max_length=255, default="")
    concessionary = models.CharField(max_length=255, default="")
    vigilant_body = models.CharField(max_length=255, default="")

    #maintenance
    maintenance_present = models.CharField(
        choices=PresentOptions.choices,
        max_length=2,
        default=PresentOptions.NOT_NOTED,
    )

    #inspections
    inspections_present = models.CharField(
        choices=PresentOptions.choices,
        max_length=2,
        default=PresentOptions.NOT_NOTED,
    )
    #number of inspections should be a calculated field
    #last inspection date should be a calculated field
    

    ### ADD MORE ###

    class Meta:
        db_table = "level_0"
        verbose_name_plural = "Level 0 items"
        verbose_name = "Level 0"

class BridgeGeometry(models.Model):
    #change for a real geometry representation
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    level_0 = models.OneToOneField(
        "Level0",
        on_delete=models.PROTECT,
        blank=True,
        default=None
    )

    class Meta:
        db_table = "bridge_geometry"
        verbose_name_plural = "Bridges geometries"
        verbose_name = "Bridge Geometry"

class ProjectDoc(models.Model):
    #Add a real document (file) field here
    name = models.CharField(max_length=255, default="")

    level_0 = models.ForeignKey(
        "Level0",
        on_delete=models.PROTECT,
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
        on_delete=models.PROTECT,
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
        on_delete=models.PROTECT,
        blank=True,
        default=None
    )

    class Meta:
        db_table = "inspection"
        verbose_name_plural = "Inspections"
        verbose_name = "Inspection"

class Level1(models.Model):
    #enums
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
        on_delete=models.PROTECT,
        blank=True,
        default=None
    )
    class Meta:
        db_table = "level_1"
        verbose_name_plural = "Level 1 items"
        verbose_name = "Level 1"

class FormDefects(models.Model):
    piece_number = models.IntegerField(default=1)
    notes = models.TextField(default="", blank=True)
    
    level_1 = models.ForeignKey(
        "Level1",
        on_delete=models.PROTECT,
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

    #fields
    seen = models.BooleanField(default=False)
    k1 = models.CharField(
        choices=K1_Options.choices,
        max_length=10,
        null=True,
        default=None,
    )

    k2 = models.CharField(
        choices=K2_Options.choices,
        max_length=10,
        null=True,
        default=None,
    )

    n_photo = models.CharField(max_length=255, default="")
    ps = models.BooleanField(null=True, default=None)
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
        on_delete=models.CASCADE,
        blank=True,
        default=None
    )
    
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