from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic as views

from football_lovers.teams.forms import TeamUpdateForm
from football_lovers.teams.models import Team


class TeamCreateView(views.CreateView):
    template_name = 'team/team_add_page.html'
    model = Team
    fields = ('name', 'country',)
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class TeamDetailsView(views.DetailView):
    template_name = 'team/team_details_page.html'
    model = Team


class TeamUpdateView(views.UpdateView):
    model = Team
    template_name = 'team/team_update_page.html'
    form_class = TeamUpdateForm

    def get_success_url(self):
        return reverse_lazy('details team', kwargs={'pk': self.object.pk})


class TeamDeleteView(views.DeleteView):
    template_name = 'team/team_delete_page.html'
    model = Team
    success_url = reverse_lazy('home page')
