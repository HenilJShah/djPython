"""dj_url_Pattern URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from app1 import views as a1
from app2 import views as a2
from app3 import views as a3
from . import view



app1 = [
    path("app1_1/", a1.app1_home1),
    path("app2_1/", a1.app1_home2),
]

app2 = [
    path("app1_2/", a2.app2_home1),
    path("app2_2/", a2.app2_home2),
]

app3 = [
    path("app1_3/", a3.app3_home1),
    path("app2_3/", a3.app3_home2),
]



urlpatterns = [
    path('admin/', admin.site.urls),

    #    app1
    path('app_1/', include([
        path("app1_1/", a1.app1_home1),
        path("app2_1/", a1.app1_home2),
    ])),

    #    app2
    path('app_2/', include([
        path("app1_2/", a2.app2_home1),
        path("app2_2/", a2.app2_home2),
    ])),

    #    app3
    path('app_3/', include([
        path("app1_3/", a3.app3_home1),
        path("app2_3/", a3.app3_home2),
    ])),

    path("", view.home),

    # new patten
    path('demo_app1/', include(app1)),
    path('demo_app2/', include(app2)),
    path('demo_app3/', include(app3)),
]


