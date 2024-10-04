from django.contrib import admin
from .models import Parent, Child

class ChildInline(admin.TabularInline):
    model = Child

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    inlines = [ChildInline]

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    model = Child
