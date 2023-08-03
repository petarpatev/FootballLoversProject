from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from football_lovers.common.forms import StoryUpdateForm
from football_lovers.common.models import Story, Like

UserModel = get_user_model()


def home_page(request):
    users = UserModel.objects.all()
    stories = Story.objects.all()
    context = {
        'users': users,
        'stories': stories,
    }

    return render(request, 'common/home_page.html', context)


class StoryCreateView(views.CreateView):
    template_name = 'common/story_add_page.html'
    model = Story
    fields = ('title', 'content',)
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class StoryDetailsView(views.DetailView):
    template_name = 'common/story_details_page.html'
    model = Story

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['likes'] = self.object.like_set.all()


class StoryUpdateView(views.UpdateView):
    model = Story
    template_name = 'common/story_update_page.html'
    form_class = StoryUpdateForm

    def get_success_url(self):
        return reverse_lazy('details story', kwargs={'pk': self.object.pk})


class StoryDeleteView(views.DeleteView):
    template_name = 'common/story_delete_page.html'
    model = Story
    success_url = reverse_lazy('home page')


def like_story(request, story_pk):
    story = Story.objects.filter(pk=story_pk).get()
    liked_obj = Like.objects.filter(to_story_id=story_pk, user=request.user).first()

    if liked_obj:
        liked_obj.delete()
    else:
        like = Like.objects.create(to_story=story, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{story_pk}')
