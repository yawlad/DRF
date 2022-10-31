from http import client
from urllib import request, response
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from authapp.models import User
from .views import ProjectModelViewSet, ToDoModelViewSet
from .models import ToDo, Project

#------------------------------------TestCase&APIRequestFactory------------------------------------#

class TestProjectViewSet(TestCase):

    def setUp(self) -> None:
        self.url = '/api/projects/' 
        self.projects_dict = {
            'project_name': 'Example1',
            'repository_url': 'Example1',
        }
        self.projects_dict_put = {
            'project_name': 'ExamplePut',
            'repository_url': 'ExamplePut',
        }
        self.format = 'json'
        self.login = 'admin'
        self.password = 'admin'
        self.admin = User.objects.create_superuser(self.login, 'root@mail.ru', self.password)
        self.projects = Project.objects.create(project_name='Example2', repository_url= 'Example2')

        

    def test_factory_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_factory_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.projects_dict, format=self.format)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    
    def test_factory_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, self.projects_dict, format=self.format)
        force_authenticate(request, self.admin)
        
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#------------------------------------------------------------------------------------#

    def test_api_client_detail(self):
        client = APIClient()
        response = client.get(f'{self.url}{self.projects.id}/') 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_api_client_update_guest(self):
        client = APIClient()
        response = client.put(f'{self.url}{self.projects.id}/', **self.projects_dict_put) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_client_update_admin(self):
        client = APIClient()
        client.force_authenticate(user=self.admin)
        response = client.put(f'{self.url}{self.projects.id}/', self.projects_dict_put) 
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.projects.refresh_from_db()

        self.assertEqual(self.projects.project_name, self.projects_dict_put.get('project_name'))
        self.assertEqual(self.projects.repository_url, self.projects_dict_put.get('repository_url'))

        client.logout
#------------------------------------------------------------------------------------#


    def tearDown(self) -> None:
        return super().tearDown()

#-------------------------------------------APISimpleTestCase-------------------------------------------#


class MathTest(APISimpleTestCase):

    def test_sqrt(self):
        import math
        response = math.sqrt(16)
        self.assertEqual(response, 4)


#--------------------------------------------APITestCase--------------------------------------------#


class TestToDos(APITestCase):

    def setUp(self) -> None:
        self.url = '/api/todos/' 
        self.projects_dict = {
            'project_name': 'Example1',
            'repository_url': 'Example1',
        }
        self.projects_dict_put = {
            'project_name': 'ExamplePut',
            'repository_url': 'ExamplePut',
        }


        self.format = 'json'
        self.login = 'admin'
        self.password = 'admin'
        self.admin = User.objects.create_superuser(self.login, 'root@mail.ru', self.password)

        self.projects = Project.objects.create(**self.projects_dict)
        self.projects_put = Project.objects.create(**self.projects_dict_put)

        self.todos_dict = {'project_id': self.projects,'todo_name': 'TODOEXAMPLE','description': 'TODOEXAMPLE'}
        self.todos_dict_put = {'project_id': self.projects.id,'todo_name': 'TODOEXAMPLEPUT','description': 'TODOEXAMPLEPUT',}

        self.todos = ToDo.objects.create(**self.todos_dict)

    def test_api_test_case_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_api_test_case_update_guest(self):
        response = self.client.put(f'{self.url}{self.todos}/', self.todos_dict_put)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_test_case_update_admin(self):
        self.client.login(**{"username": self.login, "password": self.password})
        response = self.client.put(f'{self.url}{self.todos.id}/', self.todos_dict_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.todos.refresh_from_db()

        self.assertEqual(self.todos.todo_name, self.todos_dict_put.get('todo_name'))
        self.assertEqual(self.todos.description, self.todos_dict_put.get('description'))

        self.client.logout()

#----------------------------------------------------------------------------------------#

    def test_mixer(self): 
        todo = mixer.blend(ToDo)

        self.client.login(**{"username": self.login, "password": self.password})
        response = self.client.put(f'{self.url}{todo.id}/', self.todos_dict_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        todo.refresh_from_db()

        self.assertEqual(todo.todo_name, self.todos_dict_put.get('todo_name'))
        self.assertEqual(todo.description, self.todos_dict_put.get('description'))

        self.client.logout()

#----------------------------------------------------------------------------------------#

    def tearDown(self) -> None:
        return super().tearDown()
