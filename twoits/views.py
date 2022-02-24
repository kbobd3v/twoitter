from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

# Create your views here.

from .models import Twoit


def home_view(request, *args, **kwargs):
    # render receives request, url template, a context of variables and status code as parameters
    return render(request, 'pages/home.html', context={}, status=200)


# request defines method, args and kwargs are came as parameters used by the function
# are defined in the urls patterns urls.py
def twoit_detail_view(request, twoit_id,*args, **kwargs):
    data = {
        'id': twoit_id,
        # 'image_path': obj.image.url,
    }
    status = 200
    try:
        # object.get() method it's a built-in feature to find matching id's on db
        obj = Twoit.objects.get(id=twoit_id)
        data['content']=obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)  # json.dumps content_type='application/json'
