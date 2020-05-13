"""djwysei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from music import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import ListView
from .views import Download#new
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('events/',views.events,name='events'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('mix/',views.mix,name='mix'),
    path('emailview',views.emailview,name='emailview'),
    path('eventdetail/<int:id>',views.eventdetail,name='eventdetail'),
    path('hitcount/',include(('hitcount.urls','hitcount'),namespace='hitcount')),####new
    path('music/<int:pk>',Download.as_view(),name='download_page'),#####new
]
urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
