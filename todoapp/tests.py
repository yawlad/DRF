from http import client
from urllib import request, response
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from authapp.models import User
from .views import ProjectModelViewSet, ToDoModelViewSet
from .models import ToDo, Project

class TestProjectViewSet(TestCase):

    def setUp(self) -> None:
        self.url = '/api/projects/' 
        self.project_dict = {
            'project_name': 'Example1',
            'repository_url': 'Example1',
        }
        self.project_dict_put = {
            'project_name': 'ExamplePut',
            'repository_url': 'ExamplePut',
        }
        self.format = 'json'
        self.login = 'admin'
        self.password = 'admin'
        self.admin = User.objects.create_superuser(self.login, 'root@mail.ru', self.password)
        self.project = Project.objects.create(project_name='Example2', repository_url= 'Example2')

        

    def test_factory_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_factory_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.project_dict, format=self.format)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_factory_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.project_dict, format=self.format)
        force_authenticate(request, self.admin)
        
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#------------------------------------------------------------------------------------#

    def test_api_client_detail(self):
        client = APIClient()
        response = client.get(f'{self.url}{self.project.id}/') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_api_client_update_guest(self):
        client = APIClient()
        response = client.put(f'{self.url}{self.project.id}/', **self.project_dict_put) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_client_update_admin(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.put(f'{self.url}{self.project.id}/', self.project_dict_put) 
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.project.refresh_from_db()

        self.assertEqual(self.project.project_name, self.project_dict_put.get('project_name'))
        self.assertEqual(self.project.repository_url, self.project_dict_put.get('repository_url'))

        client.logout
#------------------------------------------------------------------------------------#


    def tearDown(self) -> None:
        return super().tearDown()

#------------------------------------------------------------------------------------#


class MathTest(APISimpleTestCase):

    def test_sqrt(self):
        import math
        response = math.sqrt(16)
        self.assertEqual(response, 4)


#------------------------------------------------------------------------------------#


class TestToDos(APITestCase):

    def setUp(self) -> None:
        self.url = '/api/todos/' 
        self.project_dict = {
            'project_name': 'Example1',
            'repository_url': 'Example1',
        }
        self.project_dict_put = {
            'project_name': 'ExamplePut',
            'repository_url': 'ExamplePut',
        }


        self.format = 'json'
        self.login = 'admin'
        self.password = 'admin'
        self.admin = User.objects.create_superuser(self.login, 'root@mail.ru', self.password)

        self.project = Project.objects.create(**self.project_dict)

        self.todo_dict = {
            'todo_name': 'TODOEXAMPLE1',
            'description': 'TODOEXAMPLE1'
        }

        self.project = Project.objects.create(**self.project_dict)
        self.todo = ToDo.objects.create(**self.todo_dict)

    def test_api_test_case_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_api_test_case_update_guest(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_test_case_update_admin(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self) -> None:
        return super().tearDown()
