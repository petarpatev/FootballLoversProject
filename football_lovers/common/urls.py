from django.urls import path, include

from football_lovers.common.views import home_page, StoryCreateView, StoryDetailsView, StoryUpdateView, StoryDeleteView, \
    like_story

urlpatterns = (
    path('', home_page, name='home page'),
    path('story/', include([
        path('like/<int:story_pk>/', like_story, name='like story'),
        path('create/', StoryCreateView.as_view(), name='create story'),
        path('<int:pk>/', StoryDetailsView.as_view(), name='details story'),
        path('<int:pk>/update/', StoryUpdateView.as_view(), name='update story'),
        path('<int:pk>/delete/', StoryDeleteView.as_view(), name='delete story'),

    ]))
)
