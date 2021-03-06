from django.contrib import admin

from .models import Tri

# Register your models here.


@admin.register(Tri)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in Tri._meta.get_fields()]