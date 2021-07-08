# Types of Views:
# 1.Function Based Views
# 2.Class Based Views


# 1.Function Based Views:
# Writer using function in python.
# Which receives as an argument HttpRequest object and returns an HttpResponse object.
# Generally divided into 4 strategies, i.e. CRUD(Create, Retrieve, Update, Delete).
# CRUD is the base of any framework one is using for development.


from django.shorcuts import render
from django.http import HttpResponse

# Create Views
def python(request):
    html = "<h2>Open my page</h2>"
    return HttpResponse(html)

def python_page1(request):
    return render(request,"python.html",{})

def python_page2(request):
    return render(request,"python2.html",{})


# templates for python.html:
'''
<html>
  <header>
    <title>Python Language</title>
  </header>
  <body>
    Python Programming Language
  </body>
</html>
'''

# templates for python2.html:
'''
<html>
  <header>
    <title>Django Framework</title>
  </header>
  <body>
    <h2>Python Language</h2>
    <h3>Django is python's framework</h3>
  </body>
</html>
'''