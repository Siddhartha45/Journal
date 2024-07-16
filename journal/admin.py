from django.contrib import admin

from .models import Journal, Images, Itinerary


admin.site.register(Journal)
admin.site.register(Images)
admin.site.register(Itinerary)