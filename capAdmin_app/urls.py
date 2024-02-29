from django.urls import path
from  .views import *

app_name = "capAdmin_app"


urlpatterns = [
    path('', admin_base, name='admin_base'),
    path('profile/', profile, name='profile'),
    path('profile_list/', profile_list, name='profile_list'),

]