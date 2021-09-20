import pytest
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
            "year": 0
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
            "year": 0
        }

        api_client = APIClient()
        intermediary = api_client.post(
            '/box-abbreviation/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/box-abbreviation/4/')
        assert response.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestPublicWorkerEndpoints:
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
            '/public-worker/', data=data,
            header={"Content-Type": "application/json"})
        assert response.status_code == 201

    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/public-worker/')
        assert response.status_code == 200

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
            '/public-worker/', data=data2,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.get('/public-worker/2/')
        assert response.status_code == 200

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
            '/public-worker/', data=data3,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.put(
            '/public-worker/3/', data=data4,
            header={"Content-Type": "application/json"})
        assert response.status_code == 200

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
            '/public-worker/', data=data5,
            header={"Content-Type": "application/json"})
        assert intermediary.status_code == 201
        response = api_client.delete('/public-worker/4/')
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
class TestshelfEndpoints:
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

    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/shelf/')
        assert response.status_code == 200

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
class TestStatusEndpoints:
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

    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/status/')
        assert response.status_code == 200

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


@pytest.mark.django_db(transaction=False)
class TestFrequencySheetsEndpoints:
    def test_create(self):
        data_shelf = {
            "shelfe_number": 1,
            "shelfp_number": 1
        }

        data_abbreviation = {
            "number": 123,
            "abbreviation": "SGA",
            "name": "SAGA",
            "year": 2020
        }

        api_client = APIClient()

        response_shelf = api_client.post(
            '/shelf/', data=data_shelf,
            header={"Content-Type": "application/json"})
        assert response_shelf.status_code == 201

        response_abbreviation = api_client.post(
            '/box-abbreviation/', data=data_abbreviation,
            header={"Content-Type": "application/json"})
        assert response_abbreviation.status_code == 201

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
            "abbreviation_id": response_abbreviation.data['id'],
            "shelf_id": response_shelf.data['id']
        }

        response = api_client.post(
            '/frequency-sheet/', data=data,
            header={"Content-Type": "application/json"})

        assert response.status_code == 201

    def test_list(self):

        api_client = APIClient()
        response = api_client.get('/frequency-sheet/')
        assert response.status_code == 200

    def test_retrieve(self):
        data_shelf = {
            "shelfe_number": 1,
            "shelfp_number": 1
        }

        data_abbreviation = {
            "number": 123,
            "abbreviation": "SGA",
            "name": "SAGA",
            "year": 2020
        }

        api_client = APIClient()

        response_shelf = api_client.post(
            '/shelf/', data=data_shelf,
            header={"Content-Type": "application/json"})
        assert response_shelf.status_code == 201

        response_abbreviation = api_client.post(
            '/box-abbreviation/', data=data_abbreviation,
            header={"Content-Type": "application/json"})
        assert response_abbreviation.status_code == 201

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
            "abbreviation_id": response_abbreviation.data['id'],
            "shelf_id": response_shelf.data['id']
        }

        response = api_client.post(
            '/frequency-sheet/', data=data,
            header={"Content-Type": "application/json"})
        response = api_client.get('/frequency-sheet/{}/'.format(response.data['id']))
        assert response.status_code == 200

    def test_update(self):
        data_shelf = {
            "shelfe_number": 1,
            "shelfp_number": 1
        }

        data_abbreviation = {
            "number": 123,
            "abbreviation": "SGA",
            "name": "SAGA",
            "year": 2020
        }

        api_client = APIClient()

        response_shelf = api_client.post(
            '/shelf/', data=data_shelf,
            header={"Content-Type": "application/json"})
        assert response_shelf.status_code == 201

        response_abbreviation = api_client.post(
            '/box-abbreviation/', data=data_abbreviation,
            header={"Content-Type": "application/json"})
        assert response_abbreviation.status_code == 201

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
            "abbreviation_id": response_abbreviation.data['id'],
            "shelf_id": response_shelf.data['id']
        }

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
            "abbreviation_id": response_abbreviation.data['id'],
            "shelf_id": response_shelf.data['id']
        }

        response = api_client.post(
            '/frequency-sheet/', data=data,
            header={"Content-Type": "application/json"})
        response_2 = api_client.put(
            '/frequency-sheet/{}/'.format(response.data['id']), data=data_2,
            header={"Content-Type": "application/json"})
        assert response_2.status_code == 200

    def test_destroy(self):
        data_shelf = {
            "shelfe_number": 1,
            "shelfp_number": 1
        }

        data_abbreviation = {
            "number": 123,
            "abbreviation": "SGA",
            "name": "SAGA",
            "year": 2020
        }

        api_client = APIClient()

        response_shelf = api_client.post(
            '/shelf/', data=data_shelf,
            header={"Content-Type": "application/json"})
        assert response_shelf.status_code == 201

        response_abbreviation = api_client.post(
            '/box-abbreviation/', data=data_abbreviation,
            header={"Content-Type": "application/json"})
        assert response_abbreviation.status_code == 201

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
            "abbreviation_id": response_abbreviation.data['id'],
            "shelf_id": response_shelf.data['id']
        }

        response = api_client.post(
            '/frequency-sheet/', data=data,
            header={"Content-Type": "application/json"})
        response_2 = api_client.delete(
            '/frequency-sheet/{}/'.format(response.data['id']), data=data,
            header={"Content-Type": "application/json"})
        assert response_2.status_code == 204


# @pytest.mark.django_db(transaction=False)
# class TestAdministrativeProcessEndpoints:
#     def test_create(self):
#         data_shelf = {
#             "shelfe_number": 1,
#             "shelfp_number": 1
#         }

#         data_pw = {
#             "name": "Biel Rossi",
#             "cpf": "123456789",
#             "office": "DF",
#             "class_worker": "nao",
#             "capacity": "nao",
#             "county": "df"
#         }

#         data_abbreviation = {
#             "number": 123,
#             "abbreviation": "SGA",
#             "name": "SAGA",
#             "year": 2020
#         }

#         data_status = {
#             "filed": True,
#             "eliminated": False,
#             "sent_from": "teste",
#             "requested_document": "teste",
#             "send_date": "2021-02-01"
#         }

#         data_subject = {
#             "subject_name": "teste",
#             "temporality": "2021-02-01"
#         }

#         data_unity = {
#             "telephone_number": "1",
#             "note": "teste",
#             "unity_name": "teste",
#             "unity_abbreviation": "teste",
#             "administrative_bond": "teste",
#             "bond_abbreviation": "teste",
#             "type_of_unity": "teste",
#             "municipality": "teste"
#         }

#         api_client = APIClient()

#         response_shelf = api_client.post(
#             '/shelf/', data=data_shelf,
#             header={"Content-Type": "application/json"})
#         assert response_shelf.status_code == 201

#         response_pw = api_client.post(
#             '/public-worker/', data=data_pw,
#             header={"Content-Type": "application/json"})
#         assert response_pw.status_code == 201

#         response_abbreviation = api_client.post(
#             '/box-abbreviation/', data=data_abbreviation,
#             header={"Content-Type": "application/json"})
#         assert response_abbreviation.status_code == 201

#         response_status = api_client.post(
#             '/status/', data=data_status,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         response_subject = api_client.post(
#             '/document-subject/', data=data_subject,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         response_unity = api_client.post(
#             '/unity/', data=data_unity,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         data = {
#             "process_number": "1",
#             "sender_unity": "t",
#             "notes": "t",
#             "notice_date": "2020-11-11",
#             "interested": "t",
#             "cpf_cnpj": "1",
#             "archiving_date": "2020-11-11",
#             "reference_month_year": ["2020-11-11"],
#             "sender_worker_id": response_pw.data['id'],
#             "abbreviation_id": response_abbreviation.data['id'],
#             "shelf_id": response_shelf.data['id'],
#             "status_id": response_status.data['id'],
#             "subject_id": response_subject.data['id'],
#             "dest_unity_id": response_unity.data['id']
#         }

#         response = api_client.post(
#             '/administrative-process/', data=data,
#             header={"Content-Type": "application/json"})

#         assert response.status_code == 201

#     def test_list(self):
#         api_client = APIClient()
#         response = api_client.get('/frequency-sheet/')
#         assert response.status_code == 200

#     def test_retrieve(self):
#         data_shelf = {
#             "shelfe_number": 1,
#             "shelfp_number": 1
#         }

#         data_pw = {
#             "name": "Biel Rossi",
#             "cpf": "123456789",
#             "office": "DF",
#             "class_worker": "nao",
#             "capacity": "nao",
#             "county": "df"
#         }

#         data_abbreviation = {
#             "number": 123,
#             "abbreviation": "SGA",
#             "name": "SAGA",
#             "year": 2020
#         }

#         data_status = {
#             "filed": True,
#             "eliminated": False,
#             "sent_from": "teste",
#             "requested_document": "teste",
#             "send_date": "2021-02-01"
#         }

#         data_subject = {
#             "subject_name": "teste",
#             "temporality": "2021-02-01"
#         }

#         data_unity = {
#             "telephone_number": "1",
#             "note": "teste",
#             "unity_name": "teste",
#             "unity_abbreviation": "teste",
#             "administrative_bond": "teste",
#             "bond_abbreviation": "teste",
#             "type_of_unity": "teste",
#             "municipality": "teste"
#         }

#         api_client = APIClient()

#         response_shelf = api_client.post(
#             '/shelf/', data=data_shelf,
#             header={"Content-Type": "application/json"})
#         assert response_shelf.status_code == 201

#         response_pw = api_client.post(
#             '/public-worker/', data=data_pw,
#             header={"Content-Type": "application/json"})
#         assert response_pw.status_code == 201

#         response_abbreviation = api_client.post(
#             '/box-abbreviation/', data=data_abbreviation,
#             header={"Content-Type": "application/json"})
#         assert response_abbreviation.status_code == 201

#         response_status = api_client.post(
#             '/status/', data=data_status,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         response_subject = api_client.post(
#             '/document-subject/', data=data_subject,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         response_unity = api_client.post(
#             '/unity/', data=data_unity,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         data = {
#             "process_number": "1",
#             "sender_unity": "t",
#             "notes": "t",
#             "notice_date": "2020-11-11",
#             "interested": "t",
#             "cpf_cnpj": "1",
#             "archiving_date": "2020-11-11",
#             "reference_month_year": ["2020-11-11", "2020-11-12"],
#             "sender_worker_id": response_pw.data['id'],
#             "abbreviation_id": response_abbreviation.data['id'],
#             "shelf_id": response_shelf.data['id'],
#             "status_id": response_status.data['id'],
#             "subject_id": response_subject.data['id'],
#             "dest_unity_id": response_unity.data['id']
#         }

#         response = api_client.post(
#             '/administrative-process/', data=data,
#             header={"Content-Type": "application/json"})

#         response = api_client.get('/administrative-process/{}/'
#                                   .format(response.data['id']))
#         assert response.status_code == 200

#     def test_update(self):
#         data_shelf = {
#             "shelfe_number": 1,
#             "shelfp_number": 1
#         }

#         data_pw = {
#             "name": "Biel Rossi",
#             "cpf": "123456789",
#             "office": "DF",
#             "class_worker": "nao",
#             "capacity": "nao",
#             "county": "df"
#         }

#         data_abbreviation = {
#             "number": 123,
#             "abbreviation": "SGA",
#             "name": "SAGA",
#             "year": 2020
#         }

#         data_status = {
#             "filed": True,
#             "eliminated": False,
#             "sent_from": "teste",
#             "requested_document": "teste",
#             "send_date": "2021-02-01"
#         }

#         data_subject = {
#             "subject_name": "teste",
#             "temporality": "2021-02-01"
#         }

#         data_unity = {
#             "telephone_number": "1",
#             "note": "teste",
#             "unity_name": "teste",
#             "unity_abbreviation": "teste",
#             "administrative_bond": "teste",
#             "bond_abbreviation": "teste",
#             "type_of_unity": "teste",
#             "municipality": "teste"
#         }

#         api_client = APIClient()

#         response_shelf = api_client.post(
#             '/shelf/', data=data_shelf,
#             header={"Content-Type": "application/json"})
#         assert response_shelf.status_code == 201

#         response_pw = api_client.post(
#             '/public-worker/', data=data_pw,
#             header={"Content-Type": "application/json"})
#         assert response_pw.status_code == 201

#         response_abbreviation = api_client.post(
#             '/box-abbreviation/', data=data_abbreviation,
#             header={"Content-Type": "application/json"})
#         assert response_abbreviation.status_code == 201

#         response_status = api_client.post(
#             '/status/', data=data_status,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         response_subject = api_client.post(
#             '/document-subject/', data=data_subject,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         response_unity = api_client.post(
#             '/unity/', data=data_unity,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         data = {
#             "process_number": "1",
#             "sender_unity": "t",
#             "notes": "t",
#             "notice_date": "2020-11-11",
#             "interested": "t",
#             "cpf_cnpj": "1",
#             "archiving_date": "2020-11-11",
#             "reference_month_year": ["2020-11-11", "2020-11-12"],
#             "sender_worker_id": response_pw.data['id'],
#             "abbreviation_id": response_abbreviation.data['id'],
#             "shelf_id": response_shelf.data['id'],
#             "status_id": response_status.data['id'],
#             "subject_id": response_subject.data['id'],
#             "dest_unity_id": response_unity.data['id']
#         }

#         data = {
#             "process_number": "2",
#             "sender_unity": "t",
#             "notes": "t",
#             "notice_date": "2020-11-11",
#             "interested": "t",
#             "cpf_cnpj": "1",
#             "archiving_date": "2020-11-11",
#             "reference_month_year": ["2020-11-11", "2020-11-12"],
#             "sender_worker_id": response_pw.data['id'],
#             "abbreviation_id": response_abbreviation.data['id'],
#             "shelf_id": response_shelf.data['id'],
#             "status_id": response_status.data['id'],
#             "subject_id": response_subject.data['id'],
#             "dest_unity_id": response_unity.data['id']
#         }

#         response = api_client.post(
#             '/administrative-process/', data=data,
#             header={"Content-Type": "application/json"})
#         response_2 = api_client.put(
#             '/administrative-process/{}/'.format(response.data['id']), data=data_2,
#             header={"Content-Type": "application/json"})
#         assert response_2.status_code == 200

#     def test_destroy(self):
#         data_shelf = {
#             "shelfe_number": 1,
#             "shelfp_number": 1
#         }

#         data_pw = {
#             "name": "Biel Rossi",
#             "cpf": "123456789",
#             "office": "DF",
#             "class_worker": "nao",
#             "capacity": "nao",
#             "county": "df"
#         }

#         data_abbreviation = {
#             "number": 123,
#             "abbreviation": "SGA",
#             "name": "SAGA",
#             "year": 2020
#         }

#         data_status = {
#             "filed": True,
#             "eliminated": False,
#             "sent_from": "teste",
#             "requested_document": "teste",
#             "send_date": "2021-02-01"
#         }

#         data_subject = {
#             "subject_name": "teste",
#             "temporality": "2021-02-01"
#         }

#         data_unity = {
#             "telephone_number": "1",
#             "note": "teste",
#             "unity_name": "teste",
#             "unity_abbreviation": "teste",
#             "administrative_bond": "teste",
#             "bond_abbreviation": "teste",
#             "type_of_unity": "teste",
#             "municipality": "teste"
#         }

#         api_client = APIClient()

#         response_shelf = api_client.post(
#             '/shelf/', data=data_shelf,
#             header={"Content-Type": "application/json"})
#         assert response_shelf.status_code == 201

#         response_pw = api_client.post(
#             '/public-worker/', data=data_pw,
#             header={"Content-Type": "application/json"})
#         assert response_pw.status_code == 201

#         response_abbreviation = api_client.post(
#             '/box-abbreviation/', data=data_abbreviation,
#             header={"Content-Type": "application/json"})
#         assert response_abbreviation.status_code == 201

#         response_status = api_client.post(
#             '/status/', data=data_status,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         response_subject = api_client.post(
#             '/document-subject/', data=data_subject,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         response_unity = api_client.post(
#             '/unity/', data=data_unity,
#             header={"Content-Type": "application/json"})
#         assert response_status.status_code == 201

#         data = {
#             "process_number": "1",
#             "sender_unity": "t",
#             "notes": "t",
#             "notice_date": "2020-11-11",
#             "interested": "t",
#             "cpf_cnpj": "1",
#             "archiving_date": "2020-11-11",
#             "reference_month_year": ["2020-11-11", "2020-11-12"],
#             "sender_worker_id": response_pw.data['id'],
#             "abbreviation_id": response_abbreviation.data['id'],
#             "shelf_id": response_shelf.data['id'],
#             "status_id": response_status.data['id'],
#             "subject_id": response_subject.data['id'],
#             "dest_unity_id": response_unity.data['id']
#         }

#         response = api_client.post(
#             '/administrative-process/', data=data,
#             header={"Content-Type": "application/json"})
#         response_2 = api_client.delete(
#             '/administrative-process/{}/'.format(response.data['id']), data=data,
#             header={"Content-Type": "application/json"})
#         assert response_2.status_code == 204


@pytest.mark.django_db(transaction=False)
class TestFrequencyRelationEndpoints:
    def test_create(self):
        data_shelf = {
            "shelfe_number": 1,
            "shelfp_number": 1
        }

        data_abbreviation = {
            "number": 123,
            "abbreviation": "SGA",
            "name": "SAGA",
            "year": 2020
        }

        data_subject = {
            "document_name": "teste",
            "temporality": "2021-11-11"
        }

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

        api_client = APIClient()

        response_shelf = api_client.post(
            '/shelf/', data=data_shelf,
            header={"Content-Type": "application/json"})
        assert response_shelf.status_code == 201

        response_abbreviation = api_client.post(
            '/box-abbreviation/', data=data_abbreviation,
            header={"Content-Type": "application/json"})
        assert response_abbreviation.status_code == 201

        response_type = api_client.post(
            '/document-type/', data=data_subject,
            header={"Content-Type": "application/json"})
        assert response_type.status_code == 201

        response_sender = api_client.post(
            '/unity/', data=data_sender,
            header={"Content-Type": "application/json"})
        assert response_sender.status_code == 201

        data = {
            "process_number": "1",
            "sender_unity": response_sender.data['id'],
            "notes": "teste",
            "number": "1",
            "received_date": "2021-11-11",
            "filer_user": "teste",
            "reference_period": ["2020-11-11"],
            "abbreviation_id": response_abbreviation.data['id'],
            "shelf_id": response_shelf.data['id'],
            "document_type_id": response_type.data['id'],
        }

        response = api_client.post(
            '/frequency-relation/', data=data,
            header={"Content-Type": "application/json"})

        assert response.status_code == 201

    def test_list(self):
        api_client = APIClient()
        response = api_client.get('/frequency-relation/')
        assert response.status_code == 200

    def test_retrieve(self):
        data_shelf = {
            "shelfe_number": 1,
            "shelfp_number": 1
        }

        data_abbreviation = {
            "number": 123,
            "abbreviation": "SGA",
            "name": "SAGA",
            "year": 2020
        }

        data_subject = {
            "document_name": "teste",
            "temporality": "2021-11-11"
        }

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

        api_client = APIClient()

        response_shelf = api_client.post(
            '/shelf/', data=data_shelf,
            header={"Content-Type": "application/json"})
        assert response_shelf.status_code == 201

        response_abbreviation = api_client.post(
            '/box-abbreviation/', data=data_abbreviation,
            header={"Content-Type": "application/json"})
        assert response_abbreviation.status_code == 201

        response_type = api_client.post(
            '/document-type/', data=data_subject,
            header={"Content-Type": "application/json"})
        assert response_type.status_code == 201

        response_sender = api_client.post(
            '/unity/', data=data_sender,
            header={"Content-Type": "application/json"})
        assert response_sender.status_code == 201

        data = {
            "process_number": "1",
            "sender_unity": response_sender.data['id'],
            "notes": "teste",
            "number": "1",
            "received_date": "2021-11-11",
            "filer_user": "teste",
            "reference_period": ["2020-11-11"],
            "abbreviation_id": response_abbreviation.data['id'],
            "shelf_id": response_shelf.data['id'],
            "document_type_id": response_type.data['id'],
        }

        response = api_client.post(
            '/frequency-relation/', data=data,
            header={"Content-Type": "application/json"})
        response = api_client.get('/frequency-relation/{}/'.format(response.data['id']))
        assert response.status_code == 200

    def test_update(self):
        data_shelf = {
            "shelfe_number": 1,
            "shelfp_number": 1
        }

        data_abbreviation = {
            "number": 123,
            "abbreviation": "SGA",
            "name": "SAGA",
            "year": 2020
        }

        data_subject = {
            "document_name": "teste",
            "temporality": "2021-11-11"
        }

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

        api_client = APIClient()

        response_shelf = api_client.post(
            '/shelf/', data=data_shelf,
            header={"Content-Type": "application/json"})
        assert response_shelf.status_code == 201

        response_abbreviation = api_client.post(
            '/box-abbreviation/', data=data_abbreviation,
            header={"Content-Type": "application/json"})
        assert response_abbreviation.status_code == 201

        response_type = api_client.post(
            '/document-type/', data=data_subject,
            header={"Content-Type": "application/json"})
        assert response_type.status_code == 201

        response_sender = api_client.post(
            '/unity/', data=data_sender,
            header={"Content-Type": "application/json"})
        assert response_sender.status_code == 201

        data = {
            "process_number": "1",
            "sender_unity": response_sender.data['id'],
            "notes": "teste",
            "number": "1",
            "received_date": "2021-11-11",
            "filer_user": "teste",
            "reference_period": ["2020-11-11"],
            "abbreviation_id": response_abbreviation.data['id'],
            "shelf_id": response_shelf.data['id'],
            "document_type_id": response_type.data['id'],
        }

        data_2 = {
            "process_number": "2",
            "sender_unity": response_sender.data['id'],
            "notes": "teste",
            "number": "1",
            "received_date": "2021-11-11",
            "filer_user": "teste",
            "reference_period": ["2020-11-11"],
            "abbreviation_id": response_abbreviation.data['id'],
            "shelf_id": response_shelf.data['id'],
            "document_type_id": response_type.data['id'],
        }

        response = api_client.post(
            '/frequency-relation/', data=data,
            header={"Content-Type": "application/json"})
        response_2 = api_client.put(
            '/frequency-relation/{}/'.format(response.data['id']), data=data_2,
            header={"Content-Type": "application/json"})
        assert response_2.status_code == 200

    def test_destroy(self):
        data_shelf = {
            "shelfe_number": 1,
            "shelfp_number": 1
        }

        data_abbreviation = {
            "number": 123,
            "abbreviation": "SGA",
            "name": "SAGA",
            "year": 2020
        }

        data_subject = {
            "document_name": "teste",
            "temporality": "2021-11-11"
        }

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

        api_client = APIClient()

        response_shelf = api_client.post(
            '/shelf/', data=data_shelf,
            header={"Content-Type": "application/json"})
        assert response_shelf.status_code == 201

        response_abbreviation = api_client.post(
            '/box-abbreviation/', data=data_abbreviation,
            header={"Content-Type": "application/json"})
        assert response_abbreviation.status_code == 201

        response_type = api_client.post(
            '/document-type/', data=data_subject,
            header={"Content-Type": "application/json"})
        assert response_type.status_code == 201

        response_sender = api_client.post(
            '/unity/', data=data_sender,
            header={"Content-Type": "application/json"})
        assert response_sender.status_code == 201

        data = {
            "process_number": "1",
            "sender_unity": response_sender.data['id'],
            "notes": "teste",
            "number": "1",
            "received_date": "2021-11-11",
            "filer_user": "teste",
            "reference_period": ["2020-11-11"],
            "abbreviation_id": response_abbreviation.data['id'],
            "shelf_id": response_shelf.data['id'],
            "document_type_id": response_type.data['id'],
        }

        response = api_client.post(
            '/frequency-relation/', data=data,
            header={"Content-Type": "application/json"})

        response_2 = api_client.delete(
            '/frequency-relation/{}/'.format(response.data['id']), data=data,
            header={"Content-Type": "application/json"})
        assert response_2.status_code == 204


@pytest.mark.django_db(transaction=False)
def test_archival_relation_get():
    api_client = APIClient()
    response = api_client.get('/archival-relation/')
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_archival_relation_post():
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
        "document_url": "http://www.t.com/",
        "cover_sheet": "1",
        "filer_user": "1",
        "abbreviation_id": "",
        "shelf_id": "",
        "document_type_id": response_type.data['id']
    }

    response_archival = api_client.post(
        '/archival-relation-post/', data=data,
        format='json')
    assert response_archival.status_code == 201
