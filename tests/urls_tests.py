import pytest
import json

#from model_bakery import baker

from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.mark.django_db(transaction=False)
class TestBoxAbreviationsEndpoints:

    def test_create(self):
        data = {
            "number": 8,
            "abbreviation": "",
            "name": "",
            "year": 0
        }
        api_client = APIClient()
        response = api_client.post('http://0.0.0.0:8002/box_abbreviation/', data = data, 
        header={"Content-Type": "application/json"})
        assert response.status_code == 201