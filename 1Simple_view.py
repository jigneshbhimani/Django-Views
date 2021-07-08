# It is a python function that takes a web request and return a web response.

# This response can be the HTML contents of a webpage, redirect, XML document, image, etc...

# It contains whatever arbitrary logic is necessary to return that response.


# EXAMPLE:-
# View of current date and time.

# Import the class HttpResponse from the django.http module.
from django.http import HttpResponse

# Import datetime module
import datetime

# Define a function called current_datetime
# This is the view function.
# Each view function takes an HttpRequest object as its first parameter, which is typically named request.
def current_datetime(request):
    now = datetime.datetime.now
    html = "<html><body>It is now %s.</body></html>" % now

    # returns an HttpResponse object that contains the generated response
    # each view function is responsible for returning an HttpResponse object
    return HttpResponse(html)
    
