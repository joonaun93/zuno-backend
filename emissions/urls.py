from django.urls import path 
from .views import EmissionsView 

urlpatterns = [ path("report/", EmissionsView.as_view(), name="emissions-report") ]