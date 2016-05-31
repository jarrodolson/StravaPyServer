from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from stravalib import Client

def index(request):
    client = Client()
    url = client.authorization_url(client_id=11103,
                                   redirect_uri='http://localhost:8000/authorization')
    ##TODO: Take out of code for version control
    return HttpResponse('Hello world, You are at the Strava Auth landing page. <a href="{0}">Click Here to authorize</a>'.format(url))
    
def authorize(request):
    code = request.GET.get('code')
    print("Code", code)
    print(settings.STATIC_URL)
    client = Client()
    access_token = client.exchange_code_for_token(client_id=11103,
                                                  client_secret=settings.MYSECRETKEY,
                                                  code=code)
    return HttpResponse('Your access token is {0}'.format(access_token))
