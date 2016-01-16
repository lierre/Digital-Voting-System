from django.shortcuts import render_to_response
from voter.forms import CommissionerForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect


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

        print(commissioner_form)

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
            print('errors-------------->', commissioner_form.errors)

    # Not a HTTP POST, so we render our form using a ModelForm instance
    # These forms will be blank ready for user input
    else:
        commissioner_form = CommissionerForm()

    # Render the template depending on the context
    return render_to_response('register.html', {'commissioner_form': commissioner_form, 'registered': registered},
                              context)


