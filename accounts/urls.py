from django.urls import path

from .views import authentication as auth
from .views import registration as reg

app_name = 'accounts'
urlpatterns = [
    path('login/', auth.UserLoginView.as_view(), name='login'),
    path('logout/', auth.UserLogoutView.as_view(), name='logout'),
    path('register/', reg.RegistrationView.as_view(), name="register")
]
