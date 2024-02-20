from django.urls import path
from . views import *



urlpatterns = [
    path('', base, name='base'),
    path('home', home, name='home'),
    path('cryptocurrencies', cryptocurrencies, name='cryptocurrencies'),
    path('market', market, name='market'),
    path('trade', trade, name='trade'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('user_signin', user_signin, name='user_signin'),
    path('user_signup', user_signup, name='user_signup'),
    #path('logout', logoutRequest, name="logout"),



    #______________________________________#
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),
    path('crypto_list', crypto_list, name='crypto_list'),
    path('market_data', market_data, name='market_data'),
    path('crypto-list-data', crypto_list_data, name='crypto_list_data'),
    

]