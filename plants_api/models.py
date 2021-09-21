from django.db import models


# Create your models here.
class Plant(models.Model):
    PLANT = "plant"
    FLOWER = "flower"

    CATEGORIES = (
        (PLANT, "plant"),
        (FLOWER, "flower"),
    )

    #id = models.CharField(max_length=128, null=False, blank=False, primary_key=True, serialize=True, help_text="Unique ID (name) of plant")
    name = models.CharField(max_length=150, blank=False, null=False, default="", help_text="Name of plant")
    description = models.CharField(max_length=500, blank=True, help_text="General information about the plant")
    price = models.FloatField(blank=False, null=False, help_text="Price of plant")
    quantity = models.IntegerField(blank=False, null=False, help_text="Quantity of the plant in storage")
    category = models.CharField(max_length=100, blank=True, choices=CATEGORIES, help_text="Type of plant")
    image = models.CharField(max_length=500, blank=False, help_text="Image of plant")
    barcode = models.CharField(max_length=100, blank=False, null=False, help_text="Barcode of product")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)

    