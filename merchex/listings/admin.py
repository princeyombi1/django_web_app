from django.contrib import admin
from listings.models import Band
from listings.models import Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre', 'active', 'official_homepage')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'sold', 'year', 'type', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
