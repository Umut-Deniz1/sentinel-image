from rest_framework.test import APITestCase
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from django.contrib.auth import get_user_model
from case.api.test_utils import request_default
import os


class SentinelImageViewTests(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("api:SentinelImage-list")
        self.response = {
            "S1A_IW_SLC__1SDV_20220909T155958_20220909T160025_044930_055DEF_67D1": {
                "id": "d3377e62-60f8-470e-9f05-999d0ed1e1f7",
                "image_url": "https://apihub.copernicus.eu/apihub/odata/v1/Products('d3377e62-60f8-470e-9f05-999d0ed1e1f7')/Products('Quicklook')/$value"
            },
            "S1A_IW_SLC__1SDV_20220828T155957_20220828T160024_044755_055813_667C": {
                "id": "ae8e2c59-3060-4a48-b868-52090a1ca07d",
                "image_url": "https://apihub.copernicus.eu/apihub/odata/v1/Products('ae8e2c59-3060-4a48-b868-52090a1ca07d')/Products('Quicklook')/$value"
            },
            "S1A_IW_SLC__1SDV_20220816T155957_20220816T160024_044580_055228_85D7": {
                "id": "2efbce9a-f547-4144-b738-af0c962224a7",
                "image_url": "https://apihub.copernicus.eu/apihub/odata/v1/Products('2efbce9a-f547-4144-b738-af0c962224a7')/Products('Quicklook')/$value"
            },
            "S1A_IW_SLC__1SDV_20220804T155956_20220804T160023_044405_054C91_63B2": {
                "id": "803e4d2f-76ba-4ecf-bc78-ab4de87e621b",
                "image_url": "https://apihub.copernicus.eu/apihub/odata/v1/Products('803e4d2f-76ba-4ecf-bc78-ab4de87e621b')/Products('Quicklook')/$value"
            },
            "S1A_IW_SLC__1SDV_20220723T155955_20220723T160022_044230_05476D_C9E5": {
                "id": "2535dffc-15cf-4d95-a190-c163c16ff800",
                "image_url": "https://apihub.copernicus.eu/apihub/odata/v1/Products('2535dffc-15cf-4d95-a190-c163c16ff800')/Products('Quicklook')/$value"
            },
            "S1A_IW_SLC__1SDV_20220629T155954_20220629T160021_043880_053D02_F930": {
                "id": "b4eada0b-3202-40b9-be9b-ab6ea0f4cd9b",
                "image_url": "https://apihub.copernicus.eu/apihub/odata/v1/Products('b4eada0b-3202-40b9-be9b-ab6ea0f4cd9b')/Products('Quicklook')/$value"
            },
            "S1A_IW_SLC__1SDV_20220617T155953_20220617T160020_043705_0537BE_2FFF": {
                "id": "65b331f4-f9c2-4d9f-9abb-8a45f16df094",
                "image_url": "https://apihub.copernicus.eu/apihub/odata/v1/Products('65b331f4-f9c2-4d9f-9abb-8a45f16df094')/Products('Quicklook')/$value"
            },
            "S1A_IW_SLC__1SDV_20220605T155953_20220605T160020_043530_05328B_D7DA": {
                "id": "58a704af-f577-4dc8-bddc-b18d4f2313bd",
                "image_url": "https://apihub.copernicus.eu/apihub/odata/v1/Products('58a704af-f577-4dc8-bddc-b18d4f2313bd')/Products('Quicklook')/$value"
            },
            "S1A_IW_SLC__1SDV_20220524T155951_20220524T160018_043355_052D60_86FF": {
                "id": "041fd7df-7cf8-49b4-8089-5726c420c839",
                "image_url": "https://apihub.copernicus.eu/apihub/odata/v1/Products('041fd7df-7cf8-49b4-8089-5726c420c839')/Products('Quicklook')/$value"
            },
            "S1A_IW_SLC__1SDV_20220430T155950_20220430T160017_043005_052272_545A": {
                "id": "7bc0b6dd-1e9a-4ad7-82ce-a75bbca36c65",
                "image_url": "https://apihub.copernicus.eu/apihub/odata/v1/Products('7bc0b6dd-1e9a-4ad7-82ce-a75bbca36c65')/Products('Quicklook')/$value"
            }
            }
        self.user = baker.make(get_user_model())
        self.token = baker.make("authtoken.Token", user=self.user)
        self.user_credentials = baker.make('api.UserCredential', user=self.user, credentials = {'username':os.getenv('username'), 'password':os.getenv('password')})
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        
    def test_get_images(self):
        data = request_default.get_default_get_images_data()
        response = self.client.get(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_image(self):
        response = self.client.get(self.url + '?id=d3377e62-60f8-470e-9f05-999d0ed1e1f7')
        self.assertEqual(response.status_code, status.HTTP_200_OK)