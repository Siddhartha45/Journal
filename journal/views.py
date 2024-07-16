from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Journal, Itinerary, Images
from .serializers import JournalSerializer, ItinerarySerializer, ImageSerializer, MyJournalSerializer


class JournalViewSet(viewsets.ModelViewSet):
    """All journal lists."""
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()


class ItineraryViewSet(viewsets.ModelViewSet):
    """All itenariries."""
    serializer_class = ItinerarySerializer
    queryset = Itinerary.objects.all()


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    queryset = Images.objects.all()


class MyJournalViewSet(viewsets.ReadOnlyModelViewSet):
    """Journals with their itenarary."""
    queryset = Journal.objects.all()
    serializer_class = MyJournalSerializer