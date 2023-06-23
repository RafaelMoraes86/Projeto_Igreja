from django.contrib import admin
from Dados_fieis.models import Fiel

# Register your models here.
class FielsAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localidade','data', 'foi_a_igreja')
    list_filter = ('nome',)

admin.site.register(Fiel, FielsAdmin)