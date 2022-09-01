from django.urls import path
from myapps.views import MyAppsListView

urlpatterns = [
    path("", MyAppsListView.as_view(), name="my_apps_list"),
    ]
