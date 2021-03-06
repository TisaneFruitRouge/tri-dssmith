from rest_framework import serializers
from .models import Tri


class TriSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tri
		fields = '__all__'