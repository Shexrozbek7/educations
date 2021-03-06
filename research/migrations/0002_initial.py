# Generated by Django 4.0.5 on 2022-06-08 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('research', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='research',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='protect',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='protect',
            name='protection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='protections', related_query_name='protections', to='research.alldata'),
        ),
        migrations.AddField(
            model_name='protect',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='production',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='production',
            name='production',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', related_query_name='products', to='research.alldata'),
        ),
        migrations.AddField(
            model_name='production',
            name='type_product',
            field=models.ManyToManyField(blank=True, related_name='Product types+', to='research.producttypes'),
        ),
        migrations.AddField(
            model_name='production',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='photos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', related_query_name='photos', to='research.alldata'),
        ),
        migrations.AddField(
            model_name='photo',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='phenology',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='phenology',
            name='month_eggs',
            field=models.ManyToManyField(blank=True, to='research.months', verbose_name='Month of eggs+'),
        ),
        migrations.AddField(
            model_name='phenology',
            name='month_fungus',
            field=models.ManyToManyField(blank=True, related_name='Month of fungus+', to='research.months'),
        ),
        migrations.AddField(
            model_name='phenology',
            name='month_larva',
            field=models.ManyToManyField(blank=True, related_name='Month of larva+', to='research.months'),
        ),
        migrations.AddField(
            model_name='phenology',
            name='month_m',
            field=models.ManyToManyField(blank=True, related_name='Month of manipulation+', to='research.months'),
        ),
        migrations.AddField(
            model_name='phenology',
            name='month_mature',
            field=models.ManyToManyField(blank=True, related_name='Month of mature+', to='research.months'),
        ),
        migrations.AddField(
            model_name='phenology',
            name='phenology',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phenology', related_query_name='phenology', to='research.alldata'),
        ),
        migrations.AddField(
            model_name='phenology',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='note',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='note',
            name='notes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', related_query_name='notes', to='research.alldata'),
        ),
        migrations.AddField(
            model_name='note',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experiment',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experiment',
            name='experiments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experiments', related_query_name='experiments', to='research.alldata'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alldata',
            name='all_experiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_experiment', to='research.experiment', verbose_name='Tajribalar'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='all_note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_note', to='research.note', verbose_name='Qolyozma'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='all_phenology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_phenology', to='research.phenology', verbose_name='PHenology'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='all_photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_photo', to='research.photo', verbose_name='Rasm'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='all_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_product', to='research.production', verbose_name='Maxsulot'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='all_protect',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_protect', to='research.protect', verbose_name='Qarshi kurash'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='all_research',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_research', to='research.research', verbose_name='Zararli organizm'),
        ),
        migrations.AddField(
            model_name='alldata',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alldata',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_%(model_name)s', to=settings.AUTH_USER_MODEL),
        ),
    ]
