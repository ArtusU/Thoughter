from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Thought

def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)


def thought_list_view(request, *args, **kwargs):
    queryset = Thought.objects.all()
    thoughts_list = [{'id': thought.id, 'content': thought.content} for thought in queryset]
    data = {
        'response': thoughts_list
    }
    return JsonResponse(data)


def thought_detail_view(request, thought_id, *args, **kwargs):
    data = {
        "id": thought_id,
    }
    status = 200
    try:
        obj = Thought.objects.get(id=thought_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404

    return JsonResponse(data, status=status)
