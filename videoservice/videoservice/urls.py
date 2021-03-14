
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings


urlpatterns = [   
    url(r'^admin/',admin.site.urls),
    path('',include('courses.urls',namespace="courses")),
]