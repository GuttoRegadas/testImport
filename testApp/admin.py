from django.contrib import admin
from .models import EmailTeste
#from testApp.models import EmailTeste
# Register your models here.
@admin.register(EmailTeste)
class EmailTesteAdmin(admin.ModelAdmin):
    fields = ['email',]
    list_display = ('email',)