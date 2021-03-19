from django.db import models

class Tri(models.Model):
	of        = models.TextField(default="")
	symbol    = models.TextField(default="")
	client    = models.TextField(default="")
	defaut    = models.TextField(default="")
	a_trier   = models.IntegerField(default=0)
	bonnes    = models.IntegerField(default=0)
	mauvaises = models.IntegerField(default=0)
	date      = models.DateField(auto_now=True) 
	est_trie  = models.BooleanField(default=False)

	dans_excel = models.BooleanField(default=False)
