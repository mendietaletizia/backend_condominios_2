from django.urls import path
from .views import LoginView, LogoutView, CreateUserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
]
