from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('football_lovers.accounts.urls')),
    path('', include('football_lovers.common.urls')),
    path('footballers/', include('football_lovers.footballers.urls')),
    path('stadiums/', include('football_lovers.stadiums.urls')),
    path('teams/', include('football_lovers.teams.urls')),
]
