from numpy import source
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Research,PHenology,Photo,Production,ProductTypes,Experiment,AllData,Note,Plants,Protect


class ResearchSerializer(ModelSerializer):
    
    class Meta:
        model = Research
        fields=['id','quarantine_type','name_latin','name_uzb','type','description','status','country','confirmation_status']
        extra_kwargs = {
            'quarantine_type': {'required': True},
            'name_latin': {'required': True},
            'name_uzb': {'required': True},
            'type': {'required': True},
            'description': {'required': True},
            'country': {'required': True},
            'status': {'required': False},
            'confirmation_status': {'required': False}
        }
        # exclude = ['created_by','updated_by']
    def update(self, instance, validated_data):
        instance.quarantine_type = validated_data.get('quarantine_type', instance.quarantine_type)
        instance.name_latin = validated_data.get('name_latin', instance.name_latin)
        instance.name_uzb = validated_data.get('name_uzb', instance.name_uzb)
        instance.type = validated_data.get('type', instance.type)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.confirmation_status = validated_data.get('confirmation_status', instance.confirmation_status)
        instance.country.clear()
        #instance.country = validated_data.get('country', instance.country)
        for country in validated_data.get('country'):
            instance.country.add(country)

        instance.save()
        return instance

class PHenologySerializer(ModelSerializer):
    class Meta:
        model = PHenology
        fields="__all__"
        # exclude = ['created_by','updated_by']
    def update(self, instance, validated_data):
        instance.pheno_status = validated_data.get('pheno_status', instance.pheno_status)
        """Fenologiyasi"""
        instance.eggs = validated_data.get('eggs', instance.eggs)
        instance.day_eggs = validated_data.get('day_eggs', instance.day_eggs)
        """Lichinka"""
        instance.larva = validated_data.get('larva', instance.larva)
        instance.day_larva = validated_data.get('day_larva', instance.day_larva)
        """G'umbak"""
        instance.fungus = validated_data.get('fungus', instance.fungus)
        instance.day_fungus = validated_data.get('day_fungus', instance.day_fungus)
        """Yetuk Zot"""
        instance.mature = validated_data.get('mature', instance.mature)
        instance.day_mature = validated_data.get('day_mature', instance.day_mature)
        """Ko'payishi"""
        instance.manipulation = validated_data.get('manipulation', instance.manipulation)
        instance.day_m = validated_data.get('day_m', instance.day_m)
        instance.prediction = validated_data.get('prediction', instance.prediction)
        instance.confirmation_status = validated_data.get('confirmation_status', instance.confirmation_status)
        instance.month_eggs.clear()
        instance.month_larva.clear()
        instance.month_fungus.clear()
        instance.month_mature.clear()
        instance.month_m.clear()
        for eggs in validated_data.get('month_eggs'):
            instance.month_eggs.add(eggs)
        for larva in validated_data.get('month_larva'):
            instance.month_larva.add(larva)
        for fungus in validated_data.get('month_fungus'):
            instance.month_fungus.add(fungus)
        for mature in validated_data.get('month_mature'):
            instance.month_mature.add(mature)
        for month_m in validated_data.get('month_m'):
            instance.month_m.add(month_m)

        instance.save()
        return instance


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields=["id", "photo",'name']
        
        extra_kwargs = {
            'photo_status': {'required': False},
            'confirmation_status': {'required': False},
            
        }


class ProductionSerializer(ModelSerializer):
    class Meta:
        model = Production
        fields="__all__"
        extra_kwargs = {
            'product_status': {'required': True},
            'product': {'required': True},
            'type_product': {'required': True},
            'confirmation_status': {'required': True}
        }
        # exclude = ['created_by','updated_by']
    def update(self, instance, validated_data):
        instance.product_status = validated_data.get('product_status', instance.product_status)
        instance.confirmation_status = validated_data.get('confirmation_status', instance.confirmation_status)
        instance.product_hs_code = validated_data.get('product_hs_code', instance.product_hs_code)
        instance.type_product.clear()
        instance.product.clear()
        for type in validated_data.get('type_product'):
            instance.type_product.add(type)
        for product in validated_data.get('product'):
            instance.product.add(product)

        instance.save()
        return instance
        


class ProductTypesSerializer(ModelSerializer):
    class Meta:
        model = ProductTypes
        fields="__all__"


class ExperimentSerializer(ModelSerializer):
    class Meta:
        model = Experiment
        fields="__all__"
        # exclude = ['created_by','updated_by']


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields="__all__"
        # exclude = ['created_by','updated_by']


class PlantsSerializer(ModelSerializer):
    class Meta:
        model = Plants
        fields="__all__"

class ProtectSerializer(ModelSerializer):
    class Meta:
        model = Protect
        fields="__all__"
        # exclude = ['created_by','updated_by']
    def update(self, instance, validated_data):
        instance.protect_status = validated_data.get('protect_status', instance.protect_status)
        instance.agro_protect = validated_data.get('agro_protect', instance.agro_protect)
        instance.bio_protect = validated_data.get('bio_protect', instance.bio_protect)
        instance.chemistry_protect = validated_data.get('chemistry_protect', instance.chemistry_protect)
        instance.confirmation_status = validated_data.get('confirmation_status', instance.confirmation_status)

        instance.save()
        return instance


class AllDataSerializer(ModelSerializer):
    all_research = ResearchSerializer()
    all_product = ProductionSerializer()
    all_phenology = PHenologySerializer()
    all_protect = ProtectSerializer()
    photos = PhotoSerializer(source='photes', many=True, read_only=True)
    notes_out = NoteSerializer(source='notes', many=True, read_only=True)
    experiments_out = ExperimentSerializer(source='experiments', many=True, read_only=True)
    
    class Meta:
        model = AllData
        fields="__all__"
        extra_kwargs = {
            # 'photes': {'required': False},
            'product': {'required': False},
            'notes': {'required': False},
            'experiments': {'required': False}
        }
