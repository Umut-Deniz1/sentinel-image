from rest_framework.test import APITestCase
from model_bakery import baker

from case.api.models import UserCredential

class CustomerTestModel(APITestCase):

    def setUp(self):
        self.customer = baker.make(UserCredential)

    def test_using_customer(self):
        self.assertIsInstance(self.customer, UserCredential)