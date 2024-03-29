# Generated by Django 4.2.1 on 2023-06-07 11:44

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('methodology', models.CharField(default='', max_length=255)),
                ('inspection_body', models.CharField(max_length=255)),
                ('documentation', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Inspection',
                'verbose_name_plural': 'Inspections',
                'db_table': 'inspection',
            },
        ),
        migrations.CreateModel(
            name='Level0',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iop_code', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=255)),
                ('street', models.CharField(default='', max_length=255)),
                ('initial_km', models.CharField(default='', max_length=50)),
                ('final_km', models.CharField(default='', max_length=50)),
                ('prov_region', models.CharField(default='Brescia/Lombardia', max_length=255)),
                ('municipality', models.CharField(default='', max_length=255)),
                ('locality', models.CharField(default='', max_length=255)),
                ('seismicity', models.FloatField(default='', max_length=10)),
                ('coord_geo_type', models.CharField(choices=[('ETRF2000', 'ETRF2000'), ('WGS84', 'WGS84')], default='WGS84', verbose_name='Coordinates type')),
                ('center_elevation', models.FloatField(default='', max_length=20)),
                ('center_longitude', models.FloatField(default='', max_length=20)),
                ('center_latitude', models.FloatField(default='', max_length=20)),
                ('initial_elevation', models.FloatField(default='', max_length=20)),
                ('initial_longitude', models.FloatField(default='', max_length=20)),
                ('initial_latitude', models.FloatField(default='', max_length=20)),
                ('final_elevation', models.FloatField(default='', max_length=20)),
                ('final_longitude', models.FloatField(default='', max_length=20)),
                ('final_latitude', models.FloatField(default='', max_length=20)),
                ('erosion_flooding_events', models.CharField(choices=[('PR', 'Present'), ('AB', 'Absent'), ('NN', 'Not Noted')], default='NN', max_length=2)),
                ('landslide_events', models.CharField(choices=[('PR', 'Present'), ('AB', 'Absent'), ('NN', 'Not Noted')], default='NN', max_length=2)),
                ('propietary', models.CharField(default='', max_length=255)),
                ('concessionary', models.CharField(default='', max_length=255)),
                ('vigilant_body', models.CharField(default='', max_length=255)),
                ('safeguard_measures', models.CharField(default='', max_length=255)),
                ('project_author', models.CharField(default='', max_length=255)),
                ('landscape_plans', models.CharField(default='', max_length=255, verbose_name='Inclusion of the bridge in existing/adopted Landscape Plans')),
                ('bridge_status', models.CharField(choices=[('A', 'Pienamente agibile'), ('B', 'Agibile ma con scadenze di lavori di manutenzione straordinaria'), ('C', 'Agibile ma con scadenze di lavori di manutenzione straordinaria'), ('D', 'Condizioni critiche e agibile parzialmente/lavori di manutenzione urgenti'), ('E', 'Inagibile')], max_length=1, null=True)),
                ('connection_type', models.CharField(choices=[('WATPR', "Ponte su corso d'acqua del reticolo principale"), ('WATSE', "Ponte su corso d'acqua del reticolo secondario"), ('VIAED', 'Viadotto su zona edificata'), ('VIARO', 'Viadotto su altra via di comunicazione'), ('RAILB', 'Ponte su ferrovia'), ('RAILS', "Ponte su specchi d'acqua marini"), ('VIAUR', 'Viadotto su zona urbanizzata'), ('VIAOR', 'Ponte/Viadotto su discontinuità orografica (vallata, piccoli canali, ecc.)')], max_length=5, null=True)),
                ('road_type', models.CharField(choices=[('TRRAIL', 'Autostrada o Ferrovia'), ('EXPRIM', 'Strada extraurbana principale'), ('EXSECO', 'Strada extraurbana secndaria'), ('URBFREE', 'Strada urbana di scorrimento'), ('NEROAD', 'Strada urbana di quartiere'), ('LOROAD', 'Strada locale')], max_length=7, null=True)),
                ('site_morphology', models.CharField(choices=[('CREST', 'Cresta'), ('SLOPE0', 'Pendio dolce (0-10°)'), ('SLOPE1', 'Pendio moderato (10-25°)'), ('SLOPE2', 'Pendio ripido (>25°)'), ('PLAIN', 'Pianura'), ('PLAINS', 'Pianura alla base dei versanti')], max_length=6)),
                ('extended_light', models.FloatField(max_length=10, verbose_name='Extended overall light [m]')),
                ('total_deck_width', models.FloatField(max_length=10, verbose_name='Total deck width [m]')),
                ('spans_number', models.IntegerField()),
                ('spans_light', models.FloatField(max_length=10)),
                ('track_type', models.CharField(choices=[('LINE', 'Rettilineo'), ('CURVE', 'In curva')], max_length=5)),
                ('bridge_type', models.CharField(choices=[('ARCOM', 'Arco in Muratura'), ('TRAVA', 'Travate appoggiate'), ('TRAVC', 'Travate continue'), ('SOLCA', 'Soletta in C.A.'), ('SZTCA', 'Sezione tubolare in c.a.'), ('ARCOC', 'Arco in C.A.'), ('TRAVG', 'Travate Gerber'), ('CASSP', 'Cassone in Precompresso'), ('SZTAC', 'Sezione tubolare in acciaio'), ('ARCOA', 'Arco in acciaio'), ('STOSO', 'Strallato o sospeso'), ('TRCPT', 'Travate in c.a.p. a cavi post-tesi'), ('OTHER', 'Other')], default='OTHER', max_length=5)),
                ('bridge_type_other', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Altro')),
                ('initial_aboutment_type', models.CharField(default='', max_length=255)),
                ('initial_aboutment_foundations', models.CharField(default='', max_length=255)),
                ('final_aboutment_type', models.CharField(default='', max_length=255)),
                ('final_aboutment_foundations', models.CharField(default='', max_length=255)),
                ('piles_material', models.CharField(choices=[('MA', 'Muratura'), ('CA', 'C.A.'), ('CAP', 'C.A.P.'), ('ACC', 'Acciaio'), ('MX', 'Misto (C.A./Acciaio)'), ('LEG', 'Legno'), ('OTHER', 'Other')], default='OTHER', max_length=5)),
                ('piles_material_other', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Altro')),
                ('cross_section_type', models.CharField(default='', max_length=255)),
                ('foundations_type', models.CharField(default='', max_length=255)),
                ('piles_height', models.IntegerField(max_length='2', verbose_name='Piles height [m]')),
                ('cross_section_geometry', models.CharField(default='', max_length=50)),
                ('foundations_number', models.IntegerField(max_length=2)),
                ('riverbed_evolution', models.CharField(default='', max_length=255, verbose_name='Possible evolution with respect to the river bed')),
                ('deck_material', models.CharField(choices=[('MA', 'Muratura'), ('CA', 'C.A.'), ('CAP', 'C.A.P.'), ('ACC', 'Acciaio'), ('MX', 'Misto (C.A./Acciaio)'), ('LEG', 'Legno'), ('OTHER', 'Other')], default='OTHER', max_length=5)),
                ('deck_material_other', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Altro')),
                ('slab_material', models.CharField(choices=[('CA', 'C.A.'), ('CAP', 'C.A.P.'), ('ACC', 'Acciaio'), ('MX', 'Misto (C.A./Acciaio)'), ('LEG', 'Legno'), ('OTHER', 'Other')], default='OTHER', max_length=5)),
                ('slab_material_other', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Altro')),
                ('protection_systems_type', models.CharField(default='', max_length=100)),
                ('support_equipment_type', models.CharField(default='', max_length=100)),
                ('track_width', models.FloatField(max_length=6, verbose_name='Track width [m]')),
                ('antiseimic_equipment_type', models.CharField(default='', max_length=255)),
                ('joints_type', models.CharField(default='', max_length=255)),
                ('aboutment_joint_distance', models.FloatField(default='', max_length=10)),
                ('total_joints_number', models.IntegerField()),
                ('pile_joint_distance', models.FloatField(default='', max_length=10)),
                ('masonry_vault', models.BooleanField(default='', max_length=1)),
                ('masonry_vault_description', models.CharField(default='', max_length=255)),
                ('structural_elements_repair_or_replacement', models.BooleanField(default='', max_length=1)),
                ('structural_elements_repair_or_replacement_description', models.CharField(default='', max_length=255)),
                ('roadway_widening', models.BooleanField(default='', max_length=1)),
                ('roadway_widening_description', models.CharField(default='', max_length=255)),
                ('additional_structural_elements', models.BooleanField(default='', max_length=1)),
                ('additional_structural_elements_description', models.CharField(default='', max_length=255)),
                ('geotechnical_interventions', models.BooleanField(default='', max_length=1)),
                ('geotechnical_interventions_description', models.CharField(default='', max_length=255)),
                ('mitigation_interventions', models.BooleanField(default='', max_length=1)),
                ('mitigation_interventions_description', models.CharField(default='', max_length=255)),
                ('other_interventions_description', models.CharField(default='', max_length=255)),
                ('maintenance_present', models.CharField(choices=[('PR', 'Present'), ('AB', 'Absent'), ('NN', 'Not Noted')], default='NN', max_length=2)),
                ('maintenance_plan', models.CharField(default='', max_length=255)),
                ('inspections_present', models.CharField(choices=[('PR', 'Present'), ('AB', 'Absent'), ('NN', 'Not Noted')], default='NN', max_length=2)),
                ('past_monitoring_activities', models.CharField(choices=[('PR', 'Present'), ('AB', 'Absent'), ('NN', 'Not Noted')], default='NN', max_length=2)),
                ('survey_type', models.CharField(default='', max_length=255)),
                ('monitoring_methodology', models.CharField(default='', max_length=255)),
                ('starting_date', models.DateField(default='')),
                ('last_update_date', models.DateField(default='')),
                ('finishing_date', models.DateField(default='')),
                ('equipment_type', models.CharField(default='', max_length=255)),
                ('measured_variables', models.CharField(default='', max_length=255)),
                ('significant_results', models.CharField(default='', max_length=255)),
                ('alert_level', models.CharField(default='', max_length=255)),
                ('related_documentation', models.CharField(default='', max_length=255)),
                ('attachment_n', models.CharField(default='', max_length=10)),
            ],
            options={
                'verbose_name': 'Bridge Level 0 information',
                'verbose_name_plural': 'Bridges Level 0 information',
                'db_table': 'level_0',
            },
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('structural_element', models.CharField(default='', max_length=255)),
                ('material', models.CharField(blank=True, default='', max_length=255)),
            ],
            options={
                'verbose_name': 'Piece',
                'verbose_name_plural': 'Pieces',
                'db_table': 'piece',
            },
        ),
        migrations.CreateModel(
            name='ProjectDoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('level_0', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='db_demo.level0')),
            ],
            options={
                'verbose_name': 'Project Document',
                'verbose_name_plural': 'Project Documents',
                'db_table': 'project_doc',
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='')),
                ('maintenance_type', models.CharField(default='', max_length=255)),
                ('documentation', models.CharField(default='', max_length=255)),
                ('level_0', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='db_demo.level0')),
            ],
            options={
                'verbose_name': 'Maintenance',
                'verbose_name_plural': 'Maintenance entries',
                'db_table': 'maintenance',
            },
        ),
        migrations.CreateModel(
            name='Level1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(default='', max_length=255)),
                ('km', models.CharField(default='', max_length=255)),
                ('tecnico', models.CharField(default='', max_length=255)),
                ('inspection_date', models.DateField(default='')),
                ('structure_type', models.CharField(choices=[('ARCOM', 'Arco in Muratura'), ('TRAVA', 'Travate appoggiate'), ('TRAVC', 'Travate continue'), ('SOLCA', 'Soletta in C.A.'), ('SZTCA', 'Sezione tubolare in c.a.'), ('ARCOC', 'Arco in C.A.'), ('TRAVG', 'Travate Gerber'), ('CASSP', 'Cassone in Precompresso'), ('SZTAC', 'Sezione tubolare in acciaio'), ('ARCOA', 'Arco in acciaio'), ('STOSO', 'Strallato o sospeso'), ('TRCPT', 'Travate in c.a.p. a cavi post-tesi'), ('OTHER', 'Other')], default='OTHER', max_length=5)),
                ('structure_type_other', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('inspection', models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='inspection_level_1', to='db_demo.inspection')),
            ],
            options={
                'verbose_name': 'Inspection Level 1 information',
                'verbose_name_plural': 'Inspections Level 1 information',
                'db_table': 'level_1',
            },
        ),
        migrations.AddField(
            model_name='inspection',
            name='level_0',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='db_demo.level0'),
        ),
        migrations.CreateModel(
            name='FormDefects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_number', models.IntegerField(default=1)),
                ('notes', models.TextField(blank=True, default='')),
                ('level_1', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='db_demo.level1')),
                ('piece', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='db_demo.piece')),
            ],
            options={
                'verbose_name': 'Form of Defects',
                'verbose_name_plural': 'Forms of Defects',
                'db_table': 'form_defects',
                'unique_together': {('piece', 'piece_number', 'level_1')},
            },
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('code', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.CharField(default='', max_length=255)),
                ('g', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('piece', models.ManyToManyField(to='db_demo.piece')),
            ],
            options={
                'verbose_name': 'Defect',
                'verbose_name_plural': 'Defects',
                'db_table': 'defect',
            },
        ),
        migrations.CreateModel(
            name='BridgeGeometry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(default=0)),
                ('lng', models.FloatField(default=0)),
                ('geometry_points', django.contrib.gis.db.models.fields.PointField(null=True, srid=3857)),
                ('level_0', models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='level_0_geometry', to='db_demo.level0')),
            ],
            options={
                'verbose_name': 'Bridge Geometry',
                'verbose_name_plural': 'Bridges Geometries',
                'db_table': 'bridge_geometry',
            },
        ),
        migrations.CreateModel(
            name='FormDefectsAnswer',
            fields=[
                ('seen', models.BooleanField(default=False, verbose_name='Visto')),
                ('k1', models.CharField(choices=[('0,2', '0,2'), ('0,5', '0,5'), ('1', '1'), ('None', 'Empty')], default='None', max_length=10, null=True, verbose_name='Estensione K1')),
                ('k2', models.CharField(choices=[('0,2', '0,2'), ('0,5', '0,5'), ('1', '1'), ('None', 'Empty')], default='None', max_length=10, null=True, verbose_name='Intensità K2')),
                ('n_photo', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('ps', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO'), ('None', 'Non Applica')], default='None', max_length=10, null=True, verbose_name='Pregiudica Statica (PS)')),
                ('incomplete_reason', models.CharField(choices=[('NA', 'Non Applicabile'), ('NR', 'Non Rilevabile'), ('NP', 'Non Present'), ('None', 'Empty')], default=None, max_length=10, null=True)),
                ('note', models.TextField(blank=True, default='')),
                ('defect', models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='db_demo.defect')),
                ('form_defects', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='db_demo.formdefects')),
            ],
            options={
                'verbose_name': 'Answers of Form of Defects',
                'verbose_name_plural': 'Answers of Form of Defects',
                'db_table': 'form_defects_answer',
                'unique_together': {('defect', 'form_defects')},
            },
        ),
    ]
