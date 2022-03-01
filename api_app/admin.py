from django.contrib import admin
from .models import *


class CarInLineAdmin(admin.StackedInline):
    model = Car
    extra = 0


class CarModelAdmin(admin.ModelAdmin):
    inlines = [CarInLineAdmin, ]


admin.site.register(CarModel, CarModelAdmin)
