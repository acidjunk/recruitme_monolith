from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, View
from .models import Developer, Project

from braces.views import LoginRequiredMixin, FormMessagesMixin, PermissionRequiredMixin, \
    MultiplePermissionsRequiredMixin


class DeveloperList(LoginRequiredMixin, ListView):
    template_name = 'developers/developer_list.html'
    model = Developer
    context_object_name = 'developers'

    def get_queryset(self):
        self.developers=Developer.objects.filter(is_public=True)


class DeveloperDetail(LoginRequiredMixin, DetailView):
    model = Developer
    template_name = 'developers/developer_detail.html'
    context_object_name = 'developer'
    pk_url_kwarg = 'developer_id'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        # return projects in context
        context = super(DeveloperDetail, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(developer=self.object.pk)
        return context


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'developers/project_form.html'
    context_object_name = 'project'
    fields = ['language', 'name', 'description', 'start', 'is_ended', 'end']

    def form_valid(self, form):
        # Add 404 ?
        developer=Developer.objects.get(user=self.request.user)
        form.instance.developer = developer  # Set owner to current user
        # form.instance.developer = self.request.user.develop # Set owner to current user's developer
        return super(ProjectCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('developers:developer-detail', kwargs={'slug': self.object.developer})


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'developers/project_form.html'
    context_object_name = 'project'
    pk_url_kwarg = 'project_id'
    slug_field = 'slug'
    fields = ['language', 'name', 'description', 'start', 'is_ended', 'end']

    def get_success_url(self):
        return reverse('developers:developer-detail', kwargs={'slug': self.object.developer})
