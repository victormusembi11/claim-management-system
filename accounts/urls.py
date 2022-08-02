from django.urls import path

from views import authentication as auth

app_name = 'accounts'
urlpatterns = [
    path('login/', auth.UserLoginView.as_view(), name='login'),
    path('logout/', auth.UserLogoutView.as_view(), name='logout'),
]
