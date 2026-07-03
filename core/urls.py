from django.contrib import admin
from django.urls import path
from texts.views import sentence_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sentence_page, name='sentence_page'),
]
