from django.contrib import admin
from django.urls import path
from texts.views import sentence_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sentence_page, name='sentence_page'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)