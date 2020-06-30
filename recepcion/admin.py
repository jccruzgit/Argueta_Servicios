# Register your models here.
from django.contrib import admin
from .models import Ficha, Agenda

class QuestionAdmin(admin.ModelAdmin):
    fields = ['__all__']

admin.site.register(Agenda)
