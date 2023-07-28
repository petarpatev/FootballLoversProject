from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model

from football_lovers.accounts.forms import RegisterUserForm, EditUserForm

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        user = super().form_valid(form)
        login(self.request, self.object)
        return user


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class DetailsUserView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile_details_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['footballer'] = self.object.footballer_set.first()
        context['stadium'] = self.object.stadium_set.first()
        context['team'] = self.object.team_set.first()

        return context


class EditUserView(views.UpdateView):
    model = UserModel
    template_name = 'accounts/profile_edit_page.html'
    form_class = EditUserForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class DeleteUserView(views.DeleteView):
    template_name = 'accounts/profile_delete_page.html'
    model = UserModel
    success_url = reverse_lazy('home page')
