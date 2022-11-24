from django.contrib import admin
from .models import Aluno,mini_curso

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email','data_nascimento','sexo','endereco','sexo','curso',)
    list_display_links = ('id',)

    list_per_page = 10
    search_fields = ('nome',)
    list_editable = ('nome','email','data_nascimento','sexo',)


admin.site.register(Aluno,ContatoAdmin)
admin.site.register(mini_curso)

# Register your models here.
