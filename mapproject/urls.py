"""mapproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from map.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', googleMap),
    url(r'^locationApi$',locationApi, name='locationApi'),
    url(r'^gasInfo$',gasInfo, name='gasInfo'),
    url(r'^gasWithTime/stn=([\u4e00-\u9fa5]{1,5})&date=(.{10,12})/$',gasApiV2, name='gasWithTime'),
    url(r'^sumOfGas$', sumOfGas,name="sumOfGas")

]
