from django.urls import path
from . views import *



urlpatterns = [
    path('', base, name='base'),
    path('home', home, name='home'),

    path('index/',index, name='index'),
    #______________________________________#
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    path('crypto_list', crypto_list, name='crypto_list'),
    path('market', market_data, name='market_data'),
    path('crypto-list-data', crypto_list_data, name='crypto_list_data'),
    

]