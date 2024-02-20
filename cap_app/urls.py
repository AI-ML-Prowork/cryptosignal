from django.urls import path
from . views import *



urlpatterns = [
    
    path('', home, name='home'),
    path('trade', trade, name='trade'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('user_login', user_login, name='user_login'),
    path('user_signup', user_signup, name='user_signup'),
    path('user_logout', user_logout, name="user_logout"),



    #______________________________________#
    # path('signup/', signup, name='signup'),
    # path('signin/', signin, name='signin'),
    # path('logout/', logout, name='logout'),
    path('crypto_list', crypto_list, name='crypto_list'),
    path('market_data', market_data, name='market_data'),
    path('crypto-list-data', crypto_list_data, name='crypto_list_data'),
    

]