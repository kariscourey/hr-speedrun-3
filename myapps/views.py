from django.shortcuts import render
from django.views.generic.list import ListView
from myapps.models import MyApps

class MyAppsListView(ListView):
    model = MyApps
    template_name = "myapps/list.html"
    context_object_name = "myapps_listview"
