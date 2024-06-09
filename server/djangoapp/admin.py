from djangoapp.models import admin
from .models import CarMake, CarModel


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'car_make', 'type', 'year')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name', 'make', 'model', 'car_make__name')


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
