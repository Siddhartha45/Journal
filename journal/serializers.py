from rest_framework import serializers
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Journal, Itinerary, Images


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Images
        fields = "__all__"
        # images = self.context.get('request').FILES.getlist('image')
    def create(self, validated_data):
        images = self.context.get('request').FILES.getlist('image')
        journal_id = validated_data.get('journal')
        images_list = []
        for image in images:
            image_instance = Images.objects.create(journal=journal_id, image=image)
            images_list.append(image_instance)
        return images_list

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = "__all__"


class ItinerarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Itinerary
        fields = "__all__"


class MyJournalSerializer(serializers.ModelSerializer):
    itinerary = ItinerarySerializer(many=True)
    image = ImageSerializer(many=True)
    class Meta:
        model = Journal
        fields = ["start_date", "end_date", "estimated_cost", "from_to", "description", "itinerary", "image"]


