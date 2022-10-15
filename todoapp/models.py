from unicodedata import name
from django.db import models

from django.utils.translation import gettext_lazy as _
from authapp.models import User

class Project(models.Model):
    project_name = models.CharField(_("project name"), max_length=256, unique=True)
    repository_url = models.CharField(_("repository url"), max_length=256, unique=True)
    users = models.ManyToManyField(User)


    # class Meta:
    #     """Meta definition for ProjectModel."""

    #     verbose_name = 'Project'
    #     verbose_name_plural = 'Projects'

    # def __str__(self):
    #     """Unicode representation of ProjectModel."""
    #     pass

class ToDo(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    todo_name = models.CharField(_("todo name"), max_length=256)
    description = models.TextField(_("description"))

    # class Meta:
    #     """Meta definition for ToDoModel."""

    #     verbose_name = 'ToDo'
    #     verbose_name_plural = 'ToDos'

    # def __str__(self):
    #     """Unicode representation of ToDoModel."""
    #     pass

