from django.shortcuts import render
from django.views.generic import ListView

from tasks.models import Task


class TaskListView(ListView):
    model = Task
