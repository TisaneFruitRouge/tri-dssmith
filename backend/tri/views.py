from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tri
from .serializers import TriSerializer

from .utils import insert_fichier, creer_fichier

import openpyxl
from datetime import date
import os.path

class TriView(APIView):

	def get(self, request):
		listeTris = Tri.objects.all()
		serializer = TriSerializer(listeTris, many=True)
		return Response(serializer.data)


	def post(self, request):
		data=request.data
		serializer = TriSerializer(data=data)
		
		if serializer.is_valid():
			serializer.save()
			# Création d fichier / Insertion dans le fichier excel 

			current_date  = date.today()
			current_month = current_date.month
			current_year  = current_date.year
 
			excel_path = "../excel/"+str(current_month)+"_"+str(current_year)+".xlsx"
			

			if (not os.path.isfile(excel_path)):
				# Le fichier n'existe pas encore
				creer_fichier(excel_path)

			insert_fichier(excel_path, data)


			### Fin création / insertion

			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)