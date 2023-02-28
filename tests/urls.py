import django
from django.urls import include, path
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin_resumable/', include('admin_async_upload.urls')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        (r'^media/(?P<path>.*)$', django.views.static.serve,
            {'document_root': settings.MEDIA_ROOT})
    ]
