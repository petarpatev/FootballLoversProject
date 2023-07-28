from django.urls import path, include

from football_lovers.teams.views import TeamCreateView, TeamDetailsView, TeamUpdateView, TeamDeleteView

urlpatterns = (
    path('create/', TeamCreateView.as_view(), name='create team'),
    path('<int:pk>/', include([
        path('', TeamDetailsView.as_view(), name='details team'),
        path('update/', TeamUpdateView.as_view(), name='update team'),
        path('delete/', TeamDeleteView.as_view(), name='delete team'),
    ]))
)