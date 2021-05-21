from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from .factory import *
from .models import *
from django.contrib.auth.models import User, Group

class TestDocumentRolesGet(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('documents-list')
        # create user and group
        populate_test_db_users(User, Group)
        # create docs for users
        populate_test_db_docs(Document)


    def test_sergeant_permissions(self):
        self.client.login(username='sergeant', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='private document', status_code=200)


    def test_sergeant_no_permissions(self):
        self.client.login(username='sergeant', password='123456')
        self.response = self.client.get(self.url)
        self.assertNotContains(self.response, text='secret document', status_code=200)


    def test_general_permissions(self):
        self.client.login(username='general', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='secret document', status_code=200)


    def test_general_no_permissions(self):
        self.client.login(username='general', password='123456')
        self.response = self.client.get(self.url)
        self.assertNotContains(self.response, text='top-secret document', status_code=200)


    def test_common_permissions(self):
        self.client.login(username='common', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='public document', status_code=200)


    def test_common_no_permissions(self):
        self.client.login(username='common', password='123456')
        self.response = self.client.get(self.url)
        self.assertNotContains(self.response, text='secret document', status_code=200)

    def test_president_permissions(self):
        self.client.login(username='president', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='top-secret document', status_code=200)

    def test_president_permissions_public(self):
        self.client.login(username='president', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='public document', status_code=200)

    def test_president_permissions_secret(self):
        self.client.login(username='president', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='secret document', status_code=200)

    def test_president_permissions_private(self):
        self.client.login(username='president', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, text='private document', status_code=200)


class TestDocumentRolesPost(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('documents-list')
        populate_test_db_users(User, Group)


    def test_common_no_permissions(self):
        data = {
            "title": "Doc for common",
            "text": "public document",
            "date_expired": "2021-08-08",
            "status": "active",
            "document_root": "public"
        }
        self.client.login(username='common', password='123456')
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)


    def test_sergeant_no_permissions(self):
        data = {
            "title": "Doc for common",
            "text": "public document",
            "date_expired": "2021-08-08",
            "status": "active",
            "document_root": "public"
        }
        self.client.login(username='sergeant', password='123456')
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)


    def test_general_no_permissions(self):
        data = {
            "title": "Doc for common",
            "text": "public document",
            "date_expired": "2021-08-08",
            "status": "active",
            "document_root": "secret"
        }
        self.client.login(username='general', password='123456')
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_president_permissions_secret(self):
        data = {
            "title": "Doc for president",
            "text": "secret document",
            "date_expired": "2021-08-08",
            "status": "active",
            "document_root": "secret"
        }
        self.client.login(username='president', password='123456')
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_president_permissions_topsecret(self):
        data = {
            "title": "Doc for president",
            "text": "secret document",
            "date_expired": "2021-08-08",
            "status": "active",
            "document_root": "top-secret"
        }
        self.client.login(username='president', password='123456')
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_president_permissions_private(self):
        data = {
            "title": "Doc for president",
            "text": "secret document",
            "date_expired": "2021-08-08",
            "status": "active",
            "document_root": "private"
        }
        self.client.login(username='president', password='123456')
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_president_permissions_public(self):
        data = {
            "title": "Doc for president",
            "text": "secret document",
            "date_expired": "2021-08-08",
            "status": "active",
            "document_root": "public"
        }
        self.client.login(username='president', password='123456')
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

# pk = id
# url = reverse('courses-detail', kwargs=course.id)

class TestDateExpiredDocument(APITestCase):


    def setUp(self):
        self.client = APIClient()

        self.doc1 = Document.objects.create(title='not expired doc',
                                date_expired="2021-12-31",document_root='private')
        self.doc2 = Document.objects.create(title='expired doc',
                                date_expired="2021-05-09", document_root='private',status='dead')
        populate_test_db_users(User, Group)
    def test_get_not_expired(self):
        self.url = reverse('documents-detail', kwargs={'pk': self.doc1.id})
        self.client.login(username='general',password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertContains(self.response,'active',status_code=200)
    def test_get_expired(self):
        self.url = reverse('documents-detail', kwargs={'pk': self.doc2.id})
        self.client.login(username='general',password='123456')
        self.response = self.client.get(self.url)
        print(self.response.json())
        self.assertNotContains(self.response,'dead',status_code=404)
