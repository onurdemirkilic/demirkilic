"""
URL configuration for Dion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from Service import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Home.views import HomeIndex, Ticket, Ticket_Onur, IndexIpek, IndexDion, IndexDion_Photography, IndexDion_Contact
from Service.views import Shipment, LoginService, login_request
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeIndex),
    path('index.html',HomeIndex),
    path("submit",Ticket),
    path("submit_onur",Ticket_Onur),
    path("photography",IndexDion_Photography),
    path('shipment',Shipment),
    path('control',login_request),
    path('dion',IndexDion),
    path('contact',IndexDion_Contact),
    path('contact.html',IndexDion_Contact),
    path('ipek', IndexIpek),
    path('login',LoginService,name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

handler400 = 'Service.views.Handler404'
handler403 = 'Service.views.Handler404'
handler404 = 'Service.views.Handler404'
handler500 = 'Service.views.Handler500'
