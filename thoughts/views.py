import random
from django.http.request import validate_host
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Thought
from .forms import ThoughtForm

def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)


def thought_create_view(request, *args, **kwargs):
    form = ThoughtForm(request.POST or None)
    if form.is_valid:
        obj = form.save(commit=False)
        obj.save()
        form = ThoughtForm()
    return render(request, 'components/form.html', context={'form': form})


def thought_list_view(request, *args, **kwargs):
    queryset = Thought.objects.all()
    thoughts_list = [{'id': thought.id, 'content': thought.content, "likes": random.randint(0, 1000)} for thought in queryset]
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
