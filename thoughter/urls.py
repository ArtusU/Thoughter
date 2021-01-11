from django.contrib import admin
from django.urls import path

from thoughts.views import home_view, thought_detail_view, thought_list_view, thought_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('create-thought', thought_create_view),
    path('thoughts', thought_list_view),
    path('thoughts/<int:thought_id>', thought_detail_view),
]
