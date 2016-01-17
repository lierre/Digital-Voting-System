from django.shortcuts import render_to_response
from voter.forms import CommissionerForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login


def home(request):
    return HttpResponse("Welcome to our home page")


def register(request):
    # get request context
    context = RequestContext(request)

    # A boolean value for telling the template whether registration was successful.
    # Set to False initially. Code changes value to true when registration succeeds.
    registered = False

    # If its a HTTP POST, we're interested in processing forms data
    if request.method == 'POST':
        # Attempt to grab information from the raw information
        commissioner_form = CommissionerForm(data=request.POST)

        # If the form is valid...
        if commissioner_form.is_valid():
            # save the user's form data to the database
            commissioner = commissioner_form.save()

            # Now  hash the password with the set_password method
            # Once hashed, we can update the commissioner object
            commissioner.set_password(commissioner.password)
            commissioner.save()

            registered = True

        # Invalid form - mistakes or something else ?
        # Print problems to the terminal.
        # They'll also be shown to the user
        else:
            print(commissioner_form.errors)

    # Not a HTTP POST, so we render our form using a ModelForm instance
    # These forms will be blank ready for user input
    else:
        commissioner_form = CommissionerForm()

    # Render the template depending on the context
    return render_to_response('register.html', {'commissioner_form': commissioner_form, 'registered': registered},
                              context)


def user_login(request):
    # get context for the user's request
    context = RequestContext(request)

    if request.method == 'POST':
        # If its a HTTP POST, pull out the relevant information
        # This is information is obtained from the login form
        username = request.POST['username']
        password = request.POST['password']

        # Use django machinery to attempt to see if the password/username
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we found a user object, the details are correct.
        # If None, no user with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled
            if user.is_active:
                # If the account is active and valid, log the user in.
                # Send the user back to the homepage
                login(request, user)
                return HttpResponseRedirect('/home/')
            else:
                # An inactive account was used. No login!
                return HttpResponse('Your account has been disabled')
        else:
            # Bad login details were provided so we can't login the user
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details")
    # The request was not a HTTP POST, so display the login form
    else:
        # No context variables to pass to the template system, hence
        # the blank dictionary
        return render_to_response('login.html', {}, context)
