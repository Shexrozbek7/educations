from django.shortcuts import get_object_or_404
from rest_framework import views
from .serializers import AllDataSerializer,NoteSerializer, PHenologySerializer, PhotoSerializer, ProductionSerializer, ProtectSerializer, ResearchSerializer
from .models import AllData, Note, Photo, Research,Production,PHenology,Protect,Experiment
from rest_framework.response import Response
from rest_framework import status
import json

class PhotoAllAPIViews(views.APIView):
    def get(self,request):
        photo_data = Photo.objects.all()
        photo = PhotoSerializer(photo_data,many=True).data

        return Response(photo,status = status.HTTP_200_OK)
    
    def post(self,request):
        rasm = json.loads(request.data.get('rasm'))
        return Response(data=rasm,status=status.HTTP_201_CREATED)

class AllDataAPIView(views.APIView):
    def get(self,request):
        all_data = AllData.objects.all()
        note = AllDataSerializer(all_data,many=True).data

        return Response(note,status = status.HTTP_200_OK)
    
    def post(self,request):
        sa=json.loads(request.data.get('document'))

        # print(request.FILES)
        all_data ={}
        all_data['all_research']=sa['all_research']
        all_data['all_product']=sa['all_product']
        all_data['all_phenology']=sa['all_phenology']
        all_data['all_protect']=sa['all_phenology']
        # all_data['photes']=sa['all_photo']
        # all_data['notes']=sa['all_note']
        # all_data['experiments']=sa['all_experiment']
        #print("hamma data",all_data)
        serializer = AllDataSerializer(data=all_data)
        # print("SER", serializer.data)
        if serializer.is_valid():
            print("OK", serializer.validated_data)
        #     all_research=serializer.data.get('all_research')
        #     all_product=serializer.data.get('all_product')
        #     all_phenology=serializer.data.get('all_phenology')
        #     all_protect = serializer.data.get('all_protect')
        #     all_note =serializer.data.get('all_note')
        #     all_photo =serializer.data.get('all_photo')
        #     all_experiment =serializer.data.get('all_experiment')
        #     countrys = all_research.pop('country')
        #     researchz = Research.objects.create(**all_research)
        #     for i in countrys:
        #         researchz.country.add(i)
        #     researchz.save()
        #     # Production create
        #     products = all_product.pop('product')
        #     type_products =all_product.pop('type_product')
        #     productadd = Production.objects.create(**all_product)
        #     for i in products:
        #         print(i)
        #         productadd.product.add(i)
        #     for i in type_products:
        #         print(i)
        #         productadd.type_product.add(i)
        #     productadd.save()

        #     # PHenology create
            
        #     month_eggss = all_phenology.pop('month_eggs')
        #     month_larvaa = all_phenology.pop('month_larva')
        #     month_funguss = all_phenology.pop('month_fungus')
        #     month_maturee = all_phenology.pop('month_mature')
        #     month_mm = all_phenology.pop('month_m')
        #     phenologya = PHenology.objects.create(**all_phenology)
        #     for i in month_larvaa:
        #         phenologya.month_larva.add(i)
        #     for i in month_eggss:
        #         phenologya.month_eggs.add(i)
        #     for i in month_funguss:
        #         phenologya.month_fungus.add(i)
        #     for i in month_maturee:
        #         phenologya.month_mature.add(i)
        #     for i in month_mm:
        #         phenologya.month_m.add(i)
        #     phenologya.save()
            
            
        #     #Protect create
        #     protect = Protect.objects.create(**all_protect)
        #     all_datas = AllData.objects.create(all_research = researchz,all_product = productadd,all_phenology = phenologya,all_protect= protect)
            

        #     images = request.FILES.getlist('photo')
        #     print('image File',images)
        #     for image in images:
        #         print('image File',image)
        #         Photo.objects.create(all_data = all_datas, photo=image)  
        #     notes = request.FILES.getlist('note')
        #     print('notes File',notes)
        #     for note in notes:
        #         Note.objects.create(noteo = all_datas, note=note)        
        #     experiments = request.FILES.getlist('experiment')
        #     print('experiments File',experiments)
        #     for experiment in experiments:
        #         Experiment.objects.create(experiments = all_datas, experiment=experiment)       
            
            
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            print("XATO",str(serializer.errors))
            return Response({"error": serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        # return Response(status=status.HTTP_200_OK)
            
class ResearchAPIView(views.APIView):

    def get(self,request,pk):
        research_data = get_object_or_404(Research.objects.all(), pk=pk)
        return Response(ResearchSerializer(research_data).data,status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        research_data = get_object_or_404(Research.objects.all(), pk=pk)
        data = request.data
        serializer = ResearchSerializer(instance=research_data, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            research_save = serializer.save()
        return Response(ResearchSerializer(research_save).data,status = status.HTTP_201_CREATED)

class ProductionAPIView(views.APIView):

    def get(self,request,pk):
        research_data = get_object_or_404(Production.objects.all(), pk=pk)
        return Response(ProductionSerializer(research_data).data,status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        product_data = get_object_or_404(Production.objects.all(), pk=pk)
        data = request.data
        print(request.user)
        serializer = ProductionSerializer(instance=product_data, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            product_save = serializer.save(updated_by=request.user)
        return Response(ProductionSerializer(product_save).data,status = status.HTTP_201_CREATED)

class ProtectAPIView(views.APIView):

    def get(self,request,pk):
        research_data = get_object_or_404(Protect.objects.all(), pk=pk)
        return Response(ProtectSerializer(research_data).data,status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        protect_data = get_object_or_404(Protect.objects.all(), pk=pk)
        data = request.data
        serializer = ProtectSerializer(instance=protect_data, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            protect_save = serializer.save(updated_by=request.user)
        return Response(ProtectSerializer(protect_save).data,status = status.HTTP_201_CREATED)

class PHenologyAPIView(views.APIView):

    def get(self,request,pk):
        research_data = get_object_or_404(PHenology.objects.all(), pk=pk)
        return Response(PHenologySerializer(research_data).data,status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        phenology_data = get_object_or_404(PHenology.objects.all(), pk=pk)
        data = request.data
        serializer = PHenologySerializer(instance=phenology_data, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            phenology_save = serializer.save(updated_by=request.user)
        return Response(PHenologySerializer(phenology_save).data,status = status.HTTP_201_CREATED)

class PhotoUpdateAPIView(views.APIView):

    def get(self,request,pk):
        photo_data = get_object_or_404(Photo.objects.all(), pk=pk)
        return Response(PhotoSerializer(photo_data).data,status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        photo_data = get_object_or_404(Photo.objects.all(), pk=pk)
        data = request.data
        photo = request.FILES.get('photo')
        serializer = PhotoSerializer(instance=photo_data, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            photo_save = serializer.save(photo=photo)
            return Response(PhotoSerializer(photo_save).data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors.data,status = status.HTTP_400_BAD_REQUEST)

class NoteUpdateAPIView(views.APIView):

    def get(self,request,pk):
        note_data = get_object_or_404(Note.objects.all(), pk=pk)
        return Response(NoteSerializer(note_data).data,status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        note_data = get_object_or_404(Note.objects.all(), pk=pk)
        data = request.data
        note = request.FILES.get('note')
        serializer = NoteSerializer(instance=note_data, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            note_save = serializer.save(note=note)
            return Response(NoteSerializer(note_save).data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors.data,status = status.HTTP_400_BAD_REQUEST)        