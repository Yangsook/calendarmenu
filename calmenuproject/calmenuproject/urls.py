"""calmenuproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from accounts import views as accounts_views
import calmenuapp.views
import calmenuapp.utils
import calmenuapp.tests


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', calmenuapp.views.home, name='home'),
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),

    path('event/<str:day>/mycalmenu/', calmenuapp.views.mycalmenu_list, name='mycalmenu_list'),
    path('event/<int:id>/mycalmenu_new/', calmenuapp.views.mycalmenu_new, name='mycalmenu_new'),
    path(
        "event/<int:pk>/remove",
        calmenuapp.views.mycalmenu_delete.as_view(),
        name="mycalmenu_delete",
    ),

    path('event/mymenu/', calmenuapp.views.mymenu, name='mymenu'),
    path('event/mymenu_list/', calmenuapp.views.mymenu_list, name='mymenu_list'),
    path('event/mymenu_new/', calmenuapp.views.mymenu_new, name='mymenu_new'),
    path('event/<int:pk>/mymenu_edit/', calmenuapp.views.mymenu_edit, name='mymenu_edit'),
    path(
        "event/<int:pk>/menu_remove",
        calmenuapp.views.mymenu_delete.as_view(),
        name="mymenu_delete",
    ),

    path('event/myitem/', calmenuapp.views.myitem_list, name='myitem_list'),
    path('event/<int:pk>/item_remove', calmenuapp.views.myitem_delete, name='myitem_delete'),
   
    
]
