
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url="mainapp/")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("mainapp/", include("mainapp.urls", namespace='mainapp')),
    path("authapp/", include("authapp.urls", namespace="authapp")),
    path("social_auth/", include("social_django.urls", namespace='social'))
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)