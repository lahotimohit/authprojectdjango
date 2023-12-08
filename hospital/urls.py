from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.registerPage, name='signup'),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls'))
]
