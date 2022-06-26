from django.contrib import admin

# Register your models here.

from .models import Owner, Genre, Bike, BikeInstance

# admin.site.register(Bike)
# admin.site.register(Owner)
admin.site.register(Genre)
# admin.site.register(BikeInstance)

# Define the admin class
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'id')

    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
# Register the admin class with the associated model
admin.site.register(Owner, OwnerAdmin)


class BikesInstanceInline(admin.TabularInline):
    model = BikeInstance

# Register the Admin classes for Bike using the decorator
@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'display_genre')

    inlines = [BikesInstanceInline]
    
# Register the Admin classes for BikeInstance using the decorator
@admin.register(BikeInstance)
class BikeInstanceAdmin(admin.ModelAdmin):
    list_display = ('bike','bike_model','color', 'owner', 'status', 'borrower','Card_number', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('bike', 'bike_model','color','owner', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower','Card_number')
        }),
    )