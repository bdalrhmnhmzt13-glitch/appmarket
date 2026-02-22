from django.contrib import admin
from django.urls import path
from apps import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('admin/',admin.site.urls),
path('',views.home),
path('app/<int:id>/',views.app_detail),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
