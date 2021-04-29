"""djangoProject URL Configuration

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
from django.template.defaulttags import url
from django.urls import path, include, re_path
from rest_framework import routers
from csc3170 import views
import templates
routers=routers.DefaultRouter()
routers.register(r"CreateUserGroup",views.UserAuthorization,"createuser")
routers.register(r"login",views.login,"LOGIN")
routers.register(r"ug2_fetch",views.ug2_fetch,"ug2_fetch")
routers.register(r"ug2_modify",views.ug2_modify,"ug2_modify")
routers.register(r"patent_detail",views.Pattent_Detail,"patentdetail")
routers.register(r"ug1_search_pattent",views.UG1_Search_Pattent,"ug1searchpattent")
routers.register(r"ug1_search_application",views.UG1_Search_Application,"ug1searchapplication")
routers.register(r"ug1_app_detail",views.UG1_app_detail,"ug1modify")
routers.register(r"ug1_new_application",views.UG1_new_application,"ug1newapplication")
routers.register(r"ug1_insert",views.UG1_insert,"ug1insert")
routers.register(r"ug1_modify_owner",views.UG1_modify_owner,"ug1modifyowner")
routers.register(r"ug1_modify_application",views.UG1_modify_application,"ug1modifyapplication")
routers.register(r"ug1_delete",views.UG1_delete,"ug1delete")
routers.register(r"ug3_behavior",views.UG3_Behavior,"ug3behavior")
routers.register(r"ug1_success",views.UG1_success,"ug1success")

urlpatterns = [
    path('admin/',admin.site.urls),
    path("api/",include(routers.urls)),
]