from django.contrib import admin
from .models import Club, Category, Age

# Register your models here.

class ClubAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'age',
        'teacher',
        'price',
        'term',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class AgeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Club, ClubAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Age, AgeAdmin)
