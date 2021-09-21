from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from plants_api.models import Plant


class ProfileTestBase(APITestCase):
    def setUp(self):
        self.plant_1 = Plant.objects.create(
            name = "Bacopa",
            price = 25.0,
            quantity = 5,
            image = "image1",
            barcode = "1234",
        )
        self.plant_2 = Plant.objects.create(
            name = "Baloon flower",
            price = 10.9,
            quantity = 10,
            image = "image2",
            barcode = "124",
        )


class ProfileTest(ProfileTestBase):
    def test_list_return(self):
        url = reverse("plant-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_detail_return(self):
        url = reverse("plant-detail", kwargs={"pk": self.plant_1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_plant(self):
        url = reverse("plant-list")

        response = self.client.post(
            url,
            data = {
                "name" : "Annual Vinca",
                "price" : 15.25,
                "quantity" : 12,
                "image" : "image3",
                "barcode" : "12",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_plant(self):
        self.plant_3 = Plant.objects.create(
            name = "Anna",
            price = 10.9,
            quantity = 10,
            image = "image3",
            barcode = "1244",
        )
        url = reverse("plant-detail", kwargs={"pk": self.plant_3.id})

        response = self.client.patch(
            url,
            data = {
                "quantity" : 5,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_plant(self):
        url = reverse("plant-detail", kwargs={"pk": self.plant_2.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

