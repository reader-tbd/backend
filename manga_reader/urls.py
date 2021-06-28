from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path

apipatterns = [
    path("docs/", include("apps.api_docs.urls")),
    path("manga/", include("apps.parse.urls")),
    path("auth/", include("apps.login.urls")),
]

urlpatterns = [
    path("api/", include(apipatterns)),
    re_path(r"^(?!api).*", admin.site.urls),
]
