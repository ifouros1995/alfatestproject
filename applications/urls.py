
from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'applications'


urlpatterns = [
    path('', views.new_application,name='new_application'),
    path('all_applications/', views.all_applications, name="all_applications"),
    path('updateOrder/<str:pk>/', views.updateOrder, name='updateOrder')

    #path('', views.existed_applications,name='existed_applications'),



]
