from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from football_lovers.footballers.forms import FootballerUpdateForm
from football_lovers.footballers.models import Footballer


class FootballerCreateView(views.CreateView):
    template_name = 'footballer/footballer_add_page.html'
    model = Footballer
    fields = ('name', 'age', 'team', 'nationality', 'image_url',)
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class FootballerDetailsView(views.DetailView):
    template_name = 'footballer/footballer_details_page.html'
    model = Footballer


class FootballerUpdateView(views.UpdateView):
    model = Footballer
    template_name = 'footballer/footballer_update_page.html'
    form_class = FootballerUpdateForm

    def get_success_url(self):
        return reverse_lazy('details footballer', kwargs={'pk': self.object.pk})


class FootballerDeleteView(views.DeleteView):
    template_name = 'footballer/footballer_delete_page.html'
    model = Footballer
    success_url = reverse_lazy('home page')
