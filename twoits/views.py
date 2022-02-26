import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

# Create your views here.
from .forms import TwoitForm
from .models import Twoit


def home_view(request, *args, **kwargs):
    # render receives request, url template, a context of variables and status code as parameters
    return render(request, 'pages/home.html', context={}, status=200)


def twoit_create_view(request,*args, **kwargs):
    # Here we initialize our TwoitForm class with the info sent by our form in html by post method
    # or None if there's no info coming from html form
    form = TwoitForm(request.POST or None)
    # is_valid method comes from our form model bring to us by django
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.save()
        # here we initialize the empty form class in order to leave it free for receive new data
        form = TwoitForm()
    return render(request, 'components/form.html', context={'form': form})


def twoit_list_view(request, *args, **kwargs):
    qs = Twoit.objects.all()
    twoits_list = [{'id': x.id, 'content': x.content, 'likes': random.randint(0, 10)} for x in qs]
    data = {
        'isUser': False,
        'response': twoits_list
    }
    return JsonResponse(data)


# request defines method, args and kwargs are came as parameters used by the function
# are defined in the urls patterns urls.py
def twoit_detail_view(request, twoit_id, *args, **kwargs):
    data = {
        'id': twoit_id,
        # 'image_path': obj.image.url,
    }
    status = 200
    try:
        # object.get() method it's a built-in feature to find matching id's on db
        obj = Twoit.objects.get(id=twoit_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)  # json.dumps content_type='application/json'
