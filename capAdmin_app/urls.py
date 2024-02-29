from django.urls import path
from  .views import *


urlpatterns = [
    path('', admin_base, name='admin_base'),

]