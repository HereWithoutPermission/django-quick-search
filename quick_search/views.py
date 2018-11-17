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
    # print(query)
    # return HttpResponse(query)
    results = get_search_results(query)
    context = {"search_results":results}
    return render(request, "quick_search/search_results.html", context)
    # return HttpResponse(get_search_html(query))
 
