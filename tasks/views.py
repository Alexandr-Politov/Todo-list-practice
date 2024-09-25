from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import SearchForm
from tasks.models import Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 2

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search")
        context["search_form"] = SearchForm(initial={"search": search})
        return context

    def get_queryset(self):
        queryset = Task.objects.prefetch_related("tags")
        filter_ = self.request.GET.get("search")
        if filter_:
            return queryset.filter(name__icontains=filter_)
        return queryset


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")
