from django.shortcuts import render

from .forms import ApplicationForm

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
# Create your views here.
