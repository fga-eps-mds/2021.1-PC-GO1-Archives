import pytest
from rest_framework.test import APIClient
from django.test import override_settings
from django.conf import settings


TESTS_MIDDLEWARE=[mc for mc in settings.MIDDLEWARE
                  if mc != 'archives_app.middleware.IsTokenValidMiddleware']


@pytest.mark.django_db(transaction=False)
class TestBoxAbreviationsEndpoints:
    
    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "number": 8,
            "abbreviation": "",
            "name": "",
            "year": 0
        }

        api_client = APIClient()
        response = api_client.post(
            '/box_abbreviation/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/box_abbreviation/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "number": 8,
            "abbreviation": "",
            "name": "",
            "year": 0
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/box_abbreviation/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/box_abbreviation/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "number": 8,
            "abbreviation": "",
            "name": "",
            "year": 0
        }
        data4 = {
            "number": 9,
            "abbreviation": "",
            "name": "",
            "year": 0
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/box_abbreviation/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/box_abbreviation/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data5 = {
            "number": 10,
            "abbreviation": "",
            "name": "",
            "year": 0
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/box_abbreviation/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/box_abbreviation/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestPublicWorkerEndpoints:

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "name": "",
            "cpf": "55555555550",
            "office": "",
            "class_worker": "",
            "capacity": "",
            "county": ""
        }

        api_client = APIClient()
        response = api_client.post(
            '/public_worker/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/public_worker/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "name": "",
            "cpf": "55555555551",
            "office": "",
            "class_worker": "",
            "capacity": "",
            "county": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/public_worker/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/public_worker/2/')
        assert response.status_code == 200
    
    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "name": "",
            "cpf": "55555555552",
            "office": "",
            "class_worker": "",
            "capacity": "",
            "county": ""
        }
        data4 = {
            "name": "",
            "cpf": "55555555553",
            "office": "",
            "class_worker": "",
            "capacity": "",
            "county": ""
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/public_worker/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/public_worker/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data5 = {
            "name": "",
            "cpf": "55555555554",
            "office": "",
            "class_worker": "",
            "capacity": "",
            "county": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/public_worker/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/public_worker/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestDocumentSubjectEndpoints:
    
    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "subject_name": "",
            "temporality": ""
        }

        api_client = APIClient()
        response = api_client.post(
            '/document_subject/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/document_subject/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "subject_name": "1",
            "temporality": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/document_subject/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/document_subject/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "subject_name": "2",
            "temporality": ""
        }
        data4 = {
            "subject_name": "3",
            "temporality": ""
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/document_subject/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/document_subject/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data5 = {
            "subject_name": "4",
            "temporality": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/document_subject/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/document_subject/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestDocumentTypeEndpoints:
    
    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "subject_name": "",
            "temporality": ""
        }

        api_client = APIClient()
        response = api_client.post(
            '/document_type/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/document_type/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "subject_name": "1",
            "temporality": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/document_type/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/document_type/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "subject_name": "2",
            "temporality": ""
        }
        data4 = {
            "subject_name": "3",
            "temporality": ""
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/document_type/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/document_type/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data5 = {
            "subject_name": "4",
            "temporality": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/document_type/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/document_type/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestUnityEndpoints:
    
    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "name_of_unity": "1",
            "unity_abbreviation": "",
            "administrative_bond": "",
            "bond_abbreviation": "",
            "type_of_unity": "",
            "municipality": "",
            "telephone_number": "",
            "notes": ""
        }

        api_client = APIClient()
        response = api_client.post(
            '/unity/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/unity/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "name_of_unity": "2",
            "unity_abbreviation": "",
            "administrative_bond": "",
            "bond_abbreviation": "",
            "type_of_unity": "",
            "municipality": "",
            "telephone_number": "",
            "notes": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/unity/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/unity/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "name_of_unity": "3",
            "unity_abbreviation": "",
            "administrative_bond": "",
            "bond_abbreviation": "",
            "type_of_unity": "",
            "municipality": "",
            "telephone_number": "",
            "notes": ""
        }
        data4 = {
            "name_of_unity": "4",
            "unity_abbreviation": "",
            "administrative_bond": "",
            "bond_abbreviation": "",
            "type_of_unity": "",
            "municipality": "",
            "telephone_number": "",
            "notes": ""
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/unity/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/unity/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data5 = {
            "name_of_unity": "5",
            "unity_abbreviation": "",
            "administrative_bond": "",
            "bond_abbreviation": "",
            "type_of_unity": "",
            "municipality": "",
            "telephone_number": "",
            "notes": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/unity/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/unity/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestshelfEndpoints:
    
    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "shelfe_number": 0,
            "shelfp_number": 0
        }

        api_client = APIClient()
        response = api_client.post(
            '/shelf/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/shelf/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "shelfe_number": 0,
            "shelfp_number": 3
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/shelf/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/shelf/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "shelfe_number": 0,
            "shelfp_number": 1
        }
        data4 = {
            "shelfe_number": 0,
            "shelfp_number": 2
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/shelf/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/shelf/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data5 = {
            "shelfe_number": 0,
            "shelfp_number": 4
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/shelf/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/shelf/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestFrontCoverEndpoints:
    
    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "box_abbreviation": ""
        }

        api_client = APIClient()
        response = api_client.post(
            '/front_cover/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/front_cover/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "box_abbreviation": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/front_cover/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/front_cover/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "box_abbreviation": ""
        }
        data4 = {
            "box_abbreviation": ""
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/front_cover/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/front_cover/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data5 = {
            "box_abbreviation": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/front_cover/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/front_cover/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestStatusEndpoints:
    
    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "is_filed": True,
            "unity_that_forwarded": "",
            "document_requested": "",
            "send_date": ""
        }

        api_client = APIClient()
        response = api_client.post(
            '/status/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/status/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "is_filed": False,
            "unity_that_forwarded": "",
            "document_requested": "",
            "send_date": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/status/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/status/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "is_filed": False,
            "unity_that_forwarded": "",
            "document_requested": "",
            "send_date": ""
        }
        data4 = {
            "is_filed": True,
            "unity_that_forwarded": "",
            "document_requested": "",
            "send_date": ""
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/status/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/status/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data5 = {
            "is_filed": True,
            "unity_that_forwarded": "",
            "document_requested": "",
            "send_date": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/status/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/status/4/')
        assert response.status_code == 204
