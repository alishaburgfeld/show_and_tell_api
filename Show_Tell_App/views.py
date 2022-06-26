from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    endpoint= "https://api.harvardartmuseums.org"

    # typical request: https://api.harvardartmuseums.org/RESOURCE_TYPE?apikey=e36e91da-415e-4ed1-af14-bed069389292
    # https://iiif.harvardartmuseums.org/manifests/object/299843
    # https://api.harvardartmuseums.org/image/465905
    # Find all of the objects with the word "cat" in the title and return only a few fields per record
    # r = http.request('GET', 'https://api.harvardartmuseums.org/object',
    #     fields = {
    #         'apikey': 'YOUR APIKEY HERE',
    #         'title': 'cat',
    #         'fields': 'objectnumber,title,dated'
    #     })

    # print(r.status, r.data)
    
    return HTTPResponse("Hello! Welcome to index.html!")