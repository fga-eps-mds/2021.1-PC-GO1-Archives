import pytest
from rest_framework.test import APIClient
from django.test import override_settings
from django.conf import settings
from archives_app.documents_serializers import FrequencySheetSerializer
from archives_app.documents_models import FrequencySheet
from archives_app.fields_models import Shelf, Rack, BoxAbbreviations

TESTS_MIDDLEWARE = [mc for mc in settings.MIDDLEWARE
                    if mc != 'archives_app.middleware.IsTokenValidMiddleware']


@pytest.mark.django_db(transaction=False)
class TestBoxAbreviationsEndpoints:

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        data = {
            "number": 8,
            "abbreviation": "",
            "name": "",
            "year": 2020
        }

        api_client = APIClient()
        response = api_client.post(
            '/box-abbreviation/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/box-abbreviation/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "number": 8,
            "abbreviation": "",
            "name": "",
            "year": 2020
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/box-abbreviation/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/box-abbreviation/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data3 = {
            "number": 8,
            "abbreviation": "",
            "name": "",
            "year": 2020
        }
        data4 = {
            "number": 9,
            "abbreviation": "",
            "name": "",
            "year": 2020
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/box-abbreviation/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/box-abbreviation/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200


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
            '/document-type/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/document-type/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        data2 = {
            "subject_name": "1",
            "temporality": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/document-type/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/document-type/2/')
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
            '/document-type/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/document-type/3/', data=data4,
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
            '/document-type/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/document-type/4/')
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
            "number": 0,
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
        data = {
            "number": 0,
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/shelf/', data=data,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/shelf/2/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        data = {
            "number": 0,
        }
        data_2 = {
            "number": 0,
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/shelf/', data=data,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/shelf/3/', data=data_2,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        data = {
            "number": 0,
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/shelf/', data=data,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/shelf/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestFrequencySheetsEndpoints:
    data = {
        "person_name": "teste",
        "cpf": "teste",
        "role": "teste",
        "category": "teste",
        "workplace": "teste",
        "municipal_area": "teste",
        "notes": "Nenhuma no momento",
        "process_number": "1",
        "reference_period": ["2020-11-11"],
        "abbreviation_id": "",
        "shelf_id": "",
        "rack_id": "",
        "temporality_date": "2020-11-11"
    }

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_create(self):
        api_client = APIClient()

        response = api_client.post(
            '/frequency-sheet/', data=self.data,
            header={"Content-Type": "application/json"})

        assert response.status_code == 201

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/frequency-sheet/')
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_retrieve(self):
        api_client = APIClient()

        response = api_client.post(
            '/frequency-sheet/', data=self.data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

        response = api_client.get('/frequency-sheet/{}/'.format(response.data['id']))
        assert response.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_update(self):
        api_client = APIClient()

        data_2 = {
            "person_name": "teste2",
            "cpf": "teste",
            "role": "teste",
            "category": "teste",
            "workplace": "teste",
            "municipal_area": "teste",
            "notes": "Nenhuma no momento",
            "process_number": "1",
            "reference_period": ["2020-11-11"],
            "abbreviation_id": "",
            "shelf_id": ""
        }

        response = api_client.post(
            '/frequency-sheet/', data=self.data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

        response_2 = api_client.put(
            '/frequency-sheet/{}/'.format(response.data['id']), data=data_2,
            header={"Content-Type": "application/json"})
        assert response_2.status_code == 200

    @override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
    def test_destroy(self):
        api_client = APIClient()

        response = api_client.post(
            '/frequency-sheet/', data=self.data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201
        response_2 = api_client.delete(
            '/frequency-sheet/{}/'.format(response.data['id']), data=self.data,
            header={"Content-Type": "application/json"})
        assert response_2.status_code == 204


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_archival_relation_get():
    api_client = APIClient()
    response = api_client.get('/archival-relation/')
    assert response.status_code == 200


@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def archival_relation_data():
    api_client = APIClient()

    data_sender = {
        "telephone_number": "",
        "note": "",
        "unity_name": "",
        "unity_abbreviation": "",
        "administrative_bond": "",
        "bond_abbreviation": "",
        "type_of_unity": "",
        "municipality": ""
    }

    response_sender = api_client.post(
        '/unity/', data=data_sender,
        header={"Content-Type": "application/json"})
    assert response_sender.status_code == 201

    data_type = {
        "document_name": "teste",
        "temporality": "1"
    }

    response_type = api_client.post(
        '/document-type/', data=data_type,
        header={"Content-Type": "application/json"})
    assert response_type.status_code == 201

    data = {
        "box_list": [
            {
                "number": "1",
                "year": 2020,
                "subjects_list": [
                    {
                        "name": "teste",
                        "dates": ["2020-11-11"]
                    }
                ]
            },
        ],
        "process_number": "1",
        "sender_unity": response_sender.data['id'],
        "notes": "1",
        "number": "1",
        "received_date": "2020-11-11",
        "number_of_boxes": 1,
        "document_url": "https://www.t.com/",
        "cover_sheet": "1",
        "filer_user": "1",
        "abbreviation_id": "",
        "shelf_id": "",
        "rack_id": "",
        "document_type_id": [response_type.data['id']],
        "temporality_date": "2020-11-11"
    }

    return data


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_archival_relation_get_pk():
    api_client = APIClient()

    data = archival_relation_data()

    response_archival = api_client.post(
        '/archival-relation/', data=data,
        format='json')
    assert response_archival.status_code == 201

    response_archival_get = api_client.get(
        '/archival-relation/')
    assert response_archival_get.status_code == 200

    print(response_archival_get.data[0])

    response = api_client.get('/archival-relation/{}'.format(
        response_archival_get.data[0]['id']))
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_archival_relation_get_pk_except():
    api_client = APIClient()

    response = api_client.get('/archival-relation/4000')
    assert response.status_code == 404


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_archival_relation_post():
    api_client = APIClient()

    data = archival_relation_data()

    response_archival = api_client.post(
        '/archival-relation/', data=data,
        format='json')
    assert response_archival.status_code == 201


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_search():
    api_client = APIClient()

    data = archival_relation_data()

    response_archival = api_client.post(
        '/archival-relation/', data=data,
        format='json')
    assert response_archival.status_code == 201

    response = api_client.get('/search/?filter={"process_number":"1"}')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_get_shelf_number():

    s = Shelf.objects.create(number=123)
    r = Rack.objects.create(number=123)
    b = BoxAbbreviations.objects.create(name="a")

    f = FrequencySheet.objects.create(
        person_name="teste",
        cpf="1",
        role="teste",
        category="teste",
        workplace="teste",
        municipal_area="teste",
        reference_period="2020-11-11",
        abbreviation_id=b,
        shelf_id=s,
        rack_id=r,
        notes=None,
        process_number="1"
    )

    f_s = FrequencySheetSerializer(f)
    assert f_s.get_shelf_number(f) == 123
    assert f_s.get_rack_number(f) == 123
    assert f_s.get_abbreviation_name(f) == 'a'


@pytest.mark.django_db(transaction=False)
@override_settings(MIDDLEWARE=TESTS_MIDDLEWARE)
def test_search_without_shelf():

    api_client = APIClient()

    data = archival_relation_data()

    data_shelf = {
        "number": 123,
    }

    response_shelf = api_client.post(
        '/shelf/', data=data_shelf,
        header={"Content-Type": "application/json"})
    assert response_shelf.status_code == 201

    data['shelf_id'] = response_shelf.data['id']

    response_archival = api_client.post(
        '/archival-relation/', data=data,
        format='json')
    assert response_archival.status_code == 201

    response = api_client.get('/search/?filter={"shelf_id":123}')
    assert response.status_code == 200
