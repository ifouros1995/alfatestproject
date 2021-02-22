from django.shortcuts import render

from .forms import ApplicationForm
from .models import *
from .filters import OrderFilter


# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
#from django.contrib.auth.decorators import login_required


# def newapp(request) :
#     return render(request,'applications/newapp.html')


def new_application(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        application_form = ApplicationForm(data=request.POST)
        #profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if application_form.is_valid() :

            # Save User Form to Database
            application = application_form.save()
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print('One of the forms was invalid if this else gets called.')

    else:
        # Was not an HTTP post so we just render the forms as blank.
        application_form = ApplicationForm()


    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'applications/newapp.html',
                          {'application_form':application_form,
                           'registered':registered})


def all_applications(request):

    applications = Application.objects.all()
    #orders = customer.order_set.all()
    total_applications = applications.count()
    delivered = applications.filter(status='Delivered').count()
    pending = applications.filter(status='Pending').count()


    #tableFilter = OrderFilter(request.GET, queryset=orders)
    #orders = myFilter.qs
    context = {'applications': applications, 'delivered': delivered, 'pendind': pending}
    return render(request, 'applications/all_applications.html', context)






#######################
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs

	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	return render(request, 'applications/customer.html',context)

    #return render(request, 'applications/all_applications.html')
# Create your views here.
