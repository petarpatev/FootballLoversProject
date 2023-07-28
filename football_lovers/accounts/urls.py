from django.urls import path, include

from football_lovers.accounts.views import RegisterUserView, LoginUserView, LogoutUserView, DetailsUserView, \
    EditUserView, DeleteUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', DetailsUserView.as_view(), name='profile details'),
        path('edit/', EditUserView.as_view(), name='profile edit'),
        path('delete/', DeleteUserView.as_view(), name='profile delete'),
    ])),
)
