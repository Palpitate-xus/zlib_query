from django.shortcuts import HttpResponse
import json
from zlib_query.models import *
# Create your views here.

# Create your views here.
def test(request):
    response = {'code': 200, 'msg': 'success'}
    return HttpResponse(json.dumps(response))

def book_query(request):
    book_name = request.body.decode()
    print(book_name)
    data = Books.objects.filter(title__contains = book_name)
    res = []
    for i in data:
        res.append({'id':i.zlibrary_id,'title': i.title,'author': i.author,'torrent': i.pilimi_torrent})
    response = {'code': 200, 'msg': 'success', 'data': res}
    return HttpResponse(json.dumps(response))