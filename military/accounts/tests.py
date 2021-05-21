from django.test import TestCase
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from .models import *
from django.contrib.auth.models import User, Group
from major.models import *

class TestDossierUpdate(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('dossier')
        self.user = User.objects.create_user(username='urmat', password='Urmat02D35s2km')
        self.dossier = Dossier.objects.create(full_name='Atai', date_birth='2021-05-09', gender='Female', user=self.user)
        Car.objects.create(dossier=self.dossier, mark='Subaru')
        Warcraft.objects.create(dossier=self.dossier, military_area='Desant')
        Education.objects.create(dossier=self.dossier, schoolname='AUCA')

    def test_dossier_put(self):
        self.client.login(username='urmat', password='Urmat02D35s2km')
        data = {

                "id": 8,
                "full_name": "Atay Nurmatovich",
                "date_birth": "2021-05-10",
                "gender": "Male",
                "cars": [
                    {
                        "car_id": 1,
                        "mark": "toyota"
                    }
                ],
                "schools": [
                    {
                        "edu_id": 1,
                        "schoolname": "auca"
                    }
                ],
                "warcraft": [
                    {
                        "war_id": 1,
                        "military_area": "divannie"
                    }
                ]
            }

        self.response = self.client.put(self.url, data=data, format='json')
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        self.client.login(username='urmat', password='Urmat02D35s2km')
        self.response = self.client.delete(self.url)
        print(self.response.json())
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)



