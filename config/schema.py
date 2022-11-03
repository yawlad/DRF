import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from authapp.models import User
from todoapp.models import ToDo, Project

#-----------------------------------------------------Query------------------------------------------------------------#

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(ObjectType):
    hello = graphene.String(default_value='Hi!')

    all_users = graphene.List(UserType)
    all_todos = graphene.List(ToDoType)
    all_projects = graphene.List(ProjectType)

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_todos(root, info):
        return ToDo.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

#------------------------------------------------------------------------#

    user_by_id = graphene.List(UserType, id=graphene.Int(required=False))
    project_by_project_name = graphene.List(ProjectType, project_name=graphene.String(required=False))

    def resolve_user_by_id(root, info, id=None):
        if id:
            return User.objects.get(id=id)
        return User.objects.all()

    def resolve_project_by_project_name(root, info, project_name=None):
        if project_name:
            return Project.objects.filter(project_name=project_name)
        return Project.objects.all()

#-----------------------------------------------------Mutations------------------------------------------------------------#

class ToDoUpdateMutation(graphene.Mutation):
    class Arguments:
        todo_name = graphene.String(required=True)
        id = graphene.ID()

    todo = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        todo = ToDo.objects.get(id=kwargs.get('id'))
        todo.todo_name = kwargs.get('todo_name')
        todo.save()
        return ToDoCreateMutation(todo=todo)


class ToDoCreateMutation(graphene.Mutation):
    class Arguments:
        todo_name = graphene.String(required=True)
        description = graphene.String()
        project_id = graphene.Int(required=True)
    
    todo = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        todo = ToDo.objects.create(**kwargs)
        todo.save()
        return cls(todo=todo)


class ToDoDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    todos = graphene.List(ToDoType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        ToDo.objects.get(id=kwargs.get('id')).delete()
        return ToDoCreateMutation(todos=ToDo.objects.all())



class Mutations(ObjectType):
    update_todo = ToDoUpdateMutation.Field()
    create_todo = ToDoCreateMutation.Field()
    delete_todo = ToDoDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)