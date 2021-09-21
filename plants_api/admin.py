from django.contrib import admin

from plants_api.models import Plant


class PlantAdmin(admin.ModelAdmin):
    """AAM api admin."""

    list_display = (
        "id",
        "name",
        "price",
        "quantity",
        "image",
        "barcode",
    )

admin.site.register(Plant, PlantAdmin)
