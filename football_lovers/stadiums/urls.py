from django.urls import path, include

from football_lovers.stadiums.views import StadiumCreateView, StadiumDetailsView, StadiumUpdateView, StadiumDeleteView

urlpatterns = (
    path('create/', StadiumCreateView.as_view(), name='create stadium'),
    path('<int:pk>/', include([
        path('', StadiumDetailsView.as_view(), name='details stadium'),
        path('update/', StadiumUpdateView.as_view(), name='update stadium'),
        path('delete/', StadiumDeleteView.as_view(), name='delete stadium'),
    ]))
)