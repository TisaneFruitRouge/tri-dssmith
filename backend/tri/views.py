from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tri
from .serializers import TriSerializer

import xlsxwriter


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

			new_excel_path = "../excel/"+str(data["date"])+"_"+data["of"]+".xlsx"
			new_workbook = xlsxwriter.Workbook(new_excel_path)
			new_worksheet = new_workbook.add_worksheet()
			

			data_items = data.items()

			data_keys = list(data)

			taille_data = len(data_items)
			


			list_data = [[0 for x in range(2)] for y in range(taille_data)] 

			for i in range(len(data_items)):
				list_data[i][0] = data_keys[i]
				list_data[i][1] = data[data_keys[i]]

			print(list_data)	

			for row in range(len(list_data)):
				for col in range(len(list_data[row])):
					new_worksheet.write(col, row, list_data[row][col])

			new_workbook.close()

			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)