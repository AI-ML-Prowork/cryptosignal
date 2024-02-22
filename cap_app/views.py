from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from django.conf import settings
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
import os


def home(request):
    return render(request, 'home.html')


@login_required(login_url='user_login')
def trade(request):
    return render(request, 'trade.html')


@login_required(login_url='user_login')
def about(request):
    return render(request, 'about.html')


@login_required(login_url='user_login')
def contact(request):
    return render(request, 'contact.html')








#______________________________________#


# def signup(request):
    
#     if request.user.is_authenticated:
#         return redirect('/')    
#     if request.method == 'POST':

#         first_name = request.POST.get('First_Name')
#         last_name = request.POST.get('Last_Name')
#         email = request.POST.get('Email')
#         password = request.POST.get('Password')
#         confirm_password = request.POST.get('Confirm_Password')

#         if password != confirm_password:
#             messages.error(request, 'Passwords do not match')
#             return redirect('/signup/')
        
#         # Create a new user
#         user = User.objects.create_user(
#             username=email,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             password=password,
#         )

#         login(request, user)
#         messages.success(request, 'Account created successfully')
#         return redirect('/signin/') 
    
#     return render(request, 'authentication/signup.html')



# def signin(request):

#     if request.user.is_authenticated:
#         return redirect('/')
#     if request.method == 'POST':
#         email = request.POST.get('Email')
#         password = request.POST.get('Password')
#         user = authenticate(request, username=email, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Logged in successfully')
#             return redirect('/') 
#         else:
#             messages.error(request, 'Invalid email or password')

#     return render(request, 'authentication/signin.html')


# @login_required(login_url='signin/')
# def logout(request):
#     auth_logout(request)
#     messages.success(request, 'Logged out successfully')
#     return redirect('/signin/')

@login_required(login_url='user_login')
def crypto_list(request):
    return render(request, 'crypto_list.html', {'cryptocurrencies': get_cryptocurrency_data()})



@login_required(login_url='user_login')
def crypto_list_data(request):
    return JsonResponse({'cryptocurrencies': get_cryptocurrency_data()})



def get_cryptocurrency_data():
    api_key = settings.COINMARKETCAP_API_KEY
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '2',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    cryptocurrencies = data.get('data', [])
    return cryptocurrencies

    


@login_required(login_url='user_login')
def market_data(request):

    dummy_data = {
        'bitcoin': [
            {'exchange': 'Binance', 'market_pair': 'BTC/USDT', 'category': 'spot', 'price': 48059.0},
            {'exchange': 'Huobi Global', 'market_pair': 'BTC/USDT', 'category': 'spot', 'price': 40172.92},
            {'exchange': 'OKEx', 'market_pair': 'BTC/USDT', 'category': 'spot', 'price': 47151.1},
            {'exchange': 'Kraken', 'market_pair': 'BTC/USDT', 'category': 'spot', 'price': 47928.00},
            {'exchange': 'Bitstamp', 'market_pair': 'BTC/USDT', 'category': 'spot', 'price': 47927.00},
        ],
        'ethereum': [
            {'exchange': 'Binance', 'market_pair': 'ETH/USDT', 'category': 'spot', 'price': 2500.0},
            {'exchange': 'Huobi Global', 'market_pair': 'ETH/USDT', 'category': 'spot', 'price': 2340.88},
            {'exchange': 'OKEx', 'market_pair': 'ETH/USDT', 'category': 'spot', 'price': 2489.83},
            {'exchange': 'Kraken', 'market_pair': 'ETH/USDT', 'category': 'spot', 'price': 2504.09},
            {'exchange': 'Bitstamp', 'market_pair': 'ETH/USDT', 'category': 'spot', 'price': 2500.40},
        ],
        'cardano': [
            {'exchange': 'Binance', 'market_pair': 'ADA/USDT', 'category': 'spot', 'price': 0.5403},
            {'exchange': 'Huobi Global', 'market_pair': 'ADA/USDT', 'category': 'spot', 'price': 0.51},
            {'exchange': 'OKEx', 'market_pair': 'ADA/USDT', 'category': 'spot', 'price': 0.5496},
            {'exchange': 'Kraken', 'market_pair': 'ADA/USDT', 'category': 'spot', 'price': 0.53},
            {'exchange': 'Bitstamp', 'market_pair': 'ADA/USDT', 'category': 'spot', 'price': 0.99},
        ],
        'decentraland': [
            {'exchange': 'Binance', 'market_pair': 'MANA/USDT', 'category': 'spot', 'price': 0.4692},
            {'exchange': 'Huobi Global', 'market_pair': 'MANA/USDT', 'category': 'spot', 'price': 0.4835},
            {'exchange': 'OKEx', 'market_pair': 'MANA/USDT', 'category': 'spot', 'price': 0.4614},
            {'exchange': 'Kraken', 'market_pair': 'MANA/USDT', 'category': 'spot', 'price': 0.43},
            {'exchange': 'Bitstamp', 'market_pair': 'MANA/USDT', 'category': 'spot', 'price': 0.99},
        ],
        'gala': [
            {'exchange': 'Binance', 'market_pair': 'GALA/USDT', 'category': 'spot', 'price': 0.02432},
            {'exchange': 'Huobi Global', 'market_pair': 'GALA/USDT', 'category': 'spot', 'price': 0.02},
            {'exchange': 'OKEx', 'market_pair': 'GALA/USDT', 'category': 'spot', 'price': 0.022},
            {'exchange': 'Kraken', 'market_pair': 'GALA/USDT', 'category': 'spot', 'price':  0.0215},
            {'exchange': 'Bitstamp', 'market_pair': 'GALA/USDT', 'category': 'spot', 'price': 0.99},
        ],
    }

    for crypto, data in dummy_data.items():
        reference_price = data[0]['price'] if data else 1.0
        for entry in data:
            entry['diff_amount'] = entry['price'] - reference_price
            entry['diff_percentage'] = ((entry['price'] - reference_price) / reference_price) * 100

    return render(request, 'market_data.html', {'market_data': dummy_data})



from django.shortcuts import render, redirect
from cap_app.models import CustomUser

def user_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
   
        if password != confirm_password:
            return render(request, 'authentication/user_signup.html', {'error_message': 'Passwords do not match'})     
        new_user = CustomUser(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            mobile=mobile
        )
        new_user.set_password(password)         
        new_user.save()        
        #login(request, new_user)

        return redirect('user_login')  
    else:
        return render(request, 'authentication/user_signup.html')


from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':        
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('signin_password')        
        user = authenticate(request, username=username_or_email, password=password)        
        if user is not None:            
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'authentication/user_login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'authentication/user_login.html')
    

@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect('home')





# def market_pairs_latest(request):
#     api_key = settings.COINMARKETCAP_API_KEY
#     url = 'https://pro-api.coinmarketcap.com/v1/exchange/market-pairs/latest'
    
#     headers = {
#         'Accepts': 'application/json',
#         'X-CMC_PRO_API_KEY': api_key,
#     }

#     response = requests.get(url, headers=headers)
#     data = response.json()

#     if 'data' in data:
#         exchange_data = data['data']
#         return render(request, 'market_pairs_latest.html', {'exchange_data': exchange_data})
#     else:
#         error_message = data.get('status', {}).get('error_message', 'Failed to fetch data from CoinMarketCap')
#         return render(request, 'market_pairs_latest.html', {'error_message': error_message})


# # crypto/views.py

# from django.shortcuts import render
# import requests
# from django.conf import settings

# def market_data(request):
#     api_key = settings.COINMARKETCAP_API_KEY
#     base_url = 'https://pro-api.coinmarketcap.com/v1/exchange/market-pairs/latest'

#     cryptocurrencies = ['bitcoin', 'ethereum', 'cardano', 'decentraland', 'gala']
#     exchanges = ['Binance', 'Huobi Global', 'OKEx', 'Kraken', 'Bitstamp']

#     market_data = {}

#     for crypto in cryptocurrencies:
#         market_data[crypto] = []
#         for exchange in exchanges:
#             url = f'{base_url}?symbol={crypto}/USDT&exchange={exchange}'
#             headers = {
#                 'Accepts': 'application/json',
#                 'X-CMC_PRO_API_KEY': api_key,
#             }

#             response = requests.get(url, headers=headers)
#             data = response.json()

#             if 'data' in data:
#                 market_pair = data['data']['market_pairs'][0]
#                 market_data[crypto].append({
#                     'exchange': exchange,
#                     'market_pair': market_pair['market_pair'],
#                     'category': market_pair['category'],
#                     'price': market_pair['quote']['USD']['price'],
#                 })

#     return render(request, 'market_data.html', {'market_data': market_data})



