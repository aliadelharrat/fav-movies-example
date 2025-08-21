from django.contrib import admin
from django.urls import path

from movies.views import about, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='home'),
    path("about/", about, name="about")
]
