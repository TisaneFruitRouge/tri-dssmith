from rest_framework import serializers
from .models import Tri


class TriSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tri
		fields = ['of', 'symbol', 'client', 'defaut',
				  'a_trier', 'bonnes', 'mauvaises', 'date', 'est_trie' ]