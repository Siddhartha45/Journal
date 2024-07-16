from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"journal", views.JournalViewSet)
router.register(r"itinerary", views.ItineraryViewSet)
router.register(r"images", views.ImageViewSet)
router.register(r"my-journal", views.MyJournalViewSet, basename="my_journal")

urlpatterns = router.urls

