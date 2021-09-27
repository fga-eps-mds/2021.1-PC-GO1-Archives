import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db(transaction=False)
class TestBoxAbreviationsEndpoints:
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

    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/box-abbreviation/')
        assert response.status_code == 200

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

    def test_destroy(self):
        data5 = {
            "number": 10,
            "abbreviation": "",
            "name": "",
            "year": 2020
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/box-abbreviation/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/box-abbreviation/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestDocumentSubjectEndpoints:
    def test_create(self):
        data = {
            "subject_name": "",
            "temporality": ""
        }

        api_client = APIClient()
        response = api_client.post(
            '/document-subject/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/document-subject/')
        assert response.status_code == 200

    def test_retrieve(self):
        data2 = {
            "subject_name": "1",
            "temporality": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/document-subject/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/document-subject/2/')
        assert response.status_code == 200

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
            '/document-subject/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/document-subject/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    def test_destroy(self):
        data5 = {
            "subject_name": "4",
            "temporality": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/document-subject/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/document-subject/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestDocumentTypeEndpoints:
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

    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/document-type/')
        assert response.status_code == 200

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

    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/unity/')
        assert response.status_code == 200

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
class TestShelfEndpoints:
    def test_create(self):
        data = {
            "number": 0,
        }

        api_client = APIClient()
        response = api_client.post(
            '/shelf/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/shelf/')
        assert response.status_code == 200

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
class TestFrontCoverEndpoints:
    def test_create(self):
        data = {
            "box_abbreviation": ""
        }

        api_client = APIClient()
        response = api_client.post(
            '/front-cover/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/front-cover/')
        assert response.status_code == 200

    def test_retrieve(self):
        data2 = {
            "box_abbreviation": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/front-cover/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/front-cover/2/')
        assert response.status_code == 200

    def test_update(self):
        data3 = {
            "box_abbreviation": ""
        }
        data4 = {
            "box_abbreviation": ""
        }
        api_client = APIClient()
        intermediary = api_client.post(
            '/front-cover/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/front-cover/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

    def test_destroy(self):
        data5 = {
            "box_abbreviation": ""
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/front-cover/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/front-cover/4/')
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
        "shelf_id": ""
    }

    def test_create(self):
        api_client = APIClient()

        response = api_client.post(
            '/frequency-sheet/', data=self.data,
            header={"Content-Type": "application/json"})

        assert response.status_code == 201

    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/frequency-sheet/')
        assert response.status_code == 200

    def test_retrieve(self):
        api_client = APIClient()

        response = api_client.post(
            '/frequency-sheet/', data=self.data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

        response = api_client.get('/frequency-sheet/{}/'.format(response.data['id']))
        assert response.status_code == 200

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
def test_archival_relation_get():
    api_client = APIClient()
    response = api_client.get('/archival-relation/')
    assert response.status_code == 200


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
        "temporality": "2021-11-11"
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
        "document_type_id": response_type.data['id']
    }

    return data


@pytest.mark.django_db(transaction=False)
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

    response = api_client.get('/archival-relation/{}'.format(
        response_archival_get.data[0]['id']))
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_archival_relation_post():
    api_client = APIClient()

    data = archival_relation_data()

    response_archival = api_client.post(
        '/archival-relation/', data=data,
        format='json')
    assert response_archival.status_code == 201


@pytest.mark.django_db(transaction=False)
def test_search():
    api_client = APIClient()

    data = archival_relation_data()

    response_archival = api_client.post(
        '/archival-relation/', data=data,
        format='json')
    assert response_archival.status_code == 201

    response = api_client.get('/search/?filter=%7B%22notes%22:%221%22%7D')
    assert response.status_code == 200
