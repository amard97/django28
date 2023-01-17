from django.contrib import admin
from .models import Admission
# Register your models here.
@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','age']