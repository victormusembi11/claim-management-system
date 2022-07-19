from django.urls import path, include


app_name = 'accounts'
urlpatterns = [
    path('login/', include('django.contrib.auth.urls'), name='login'),
]
