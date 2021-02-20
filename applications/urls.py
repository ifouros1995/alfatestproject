
from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'applications'


urlpatterns = [
    path('', views.new_application,name='new_application'),
    path('', views.existed_applications,name='existed_applications'),



]
