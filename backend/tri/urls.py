
from django.urls import include, path
from .views import TriView

#from rest_framework import routers


urlpatterns = [
	path('tris/', TriView.as_view()),
]