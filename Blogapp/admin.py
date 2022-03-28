from django.contrib import admin
from .models import ContactDetails, Blog

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','content','author','date']

@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ['name','email','address','phoneno','city','state']