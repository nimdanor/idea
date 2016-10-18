
from pldata.models import Pldata
from django.contrib import admin

# Register your models here.

@admin.register(Pldata)
class PldataAdmin(admin.ModelAdmin):
    list_display = ('data','stamp')


