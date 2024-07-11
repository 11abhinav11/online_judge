
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user.views import error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('problem', include('problems.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error
