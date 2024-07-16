from django.db import models


class Journal(models.Model):
    """Details of two destinations. ex: Ktm to Langtang"""
    start_date = models.DateField()
    end_date = models.DateField()
    estimated_cost = models.DecimalField(max_digits=7, decimal_places=2)
    from_to = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.from_to


class Itinerary(models.Model):
    """Routes in the journey."""
    day = models.PositiveIntegerField()
    point_a = models.CharField(max_length=255)
    point_b = models.CharField(max_length=255)
    estimated_hrs = models.CharField(max_length=3)
    description = models.TextField()
    journal = models.ForeignKey("Journal", on_delete=models.CASCADE, related_name="itinerary")


class Images(models.Model):
    """Images of the Journey."""
    journal = models.ForeignKey("Journal", on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="images")

