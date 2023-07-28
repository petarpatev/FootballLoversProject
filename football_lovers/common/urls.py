from django.urls import path

from football_lovers.common.views import home_page

urlpatterns = (
    path('', home_page, name='home page'),
)