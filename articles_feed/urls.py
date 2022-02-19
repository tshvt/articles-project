from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("posts.urls")),
    path("users/", include("users.urls")),
    path("users/", include("django.contrib.auth.urls")),
]
