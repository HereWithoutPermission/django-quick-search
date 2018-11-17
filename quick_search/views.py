from django.http import HttpResponse
from .helper import get_search_results
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

base_url = 'www.google.com/search?q='

# Create your views here.

@csrf_exempt
def search(request):
    body_json = json.loads(request.body.decode("utf-8"))
    query = body_json['query']
    results = get_search_results(query)
    context = {"search_results":results}
    return render(request, "quick_search/search_results.html", context)

def get_css(request):
    test_file = open('static/quick_search.css', 'rb')
    response = HttpResponse(content=test_file)
    return response

def get_js(request):
    content = ""
    with open("static/quick_search.js") as f:
        content = f.read()
    response = HttpResponse(content=content)
    return response

def get_html(request):
    test_file = open('static/quick_search.html', 'rb')
    response = HttpResponse(content=test_file)
    return response
