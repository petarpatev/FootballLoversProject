from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic as views

from football_lovers.stadiums.forms import StadiumUpdateForm
from football_lovers.stadiums.models import Stadium


class StadiumCreateView(views.CreateView):
    template_name = 'stadium/stadium_add_page.html'
    model = Stadium
    fields = ('name', 'country', 'capacity',)
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class StadiumDetailsView(views.DetailView):
    template_name = 'stadium/stadium_details_page.html'
    model = Stadium


class StadiumUpdateView(views.UpdateView):
    model = Stadium
    template_name = 'stadium/stadium_update_page.html'
    form_class = StadiumUpdateForm

    def get_success_url(self):
        return reverse_lazy('details stadium', kwargs={'pk': self.object.pk})


class StadiumDeleteView(views.DeleteView):
    template_name = 'stadium/stadium_delete_page.html'
    model = Stadium
    success_url = reverse_lazy('home page')
