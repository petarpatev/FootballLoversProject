from django.urls import path, include

from football_lovers.footballers.views import FootballerCreateView, FootballerDetailsView, FootballerUpdateView, \
    FootballerDeleteView

urlpatterns = (
    path('create/', FootballerCreateView.as_view(), name='create footballer'),
    path('<int:pk>/', include([
        path('', FootballerDetailsView.as_view(), name='details footballer'),
        path('update/', FootballerUpdateView.as_view(), name='update footballer'),
        path('delete/', FootballerDeleteView.as_view(), name='delete footballer'),
    ]))
)
