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
        res.append({
            'id':i.zlibrary_id,
            'title': i.title,
            'author': i.author,
            'torrent': i.pilimi_torrent,
            'in_libgen': i.in_libgen,
            'description': i.description,
            'extension': i.extension,
            'md5': i.md5,
            'md5_reported': i.md5_reported,
            'publisher': i.publisher,
            'language': i.language,
            'year': i.year,
            'edition': i.edition,
            'pages': i.pages,
            'cover_url': i.cover_url,
            'unavailable': i.unavailable,
            'date_added': i.date_added,
            'date_modified': i.date_modified,
            'filesize': i.filesize,
            'filesize_reported': i.filesize_reported,
            'series': i.series,
            'volume': i.volume
            })
        # res.append(i)
    response = {'code': 200, 'msg': 'success', 'data': res}
    return HttpResponse(json.dumps(response))