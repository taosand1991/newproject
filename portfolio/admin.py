from django.contrib import admin
from portfolio.models import Personal
# Register your models here.


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('name', 'categories',)
    list_editable = ('categories',)