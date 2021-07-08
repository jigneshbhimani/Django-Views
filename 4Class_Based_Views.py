# 2.Class Based Views:

# Simpler and efficient to manage than function-based views.
# A function-based view with tons of lines of code can be converted into a class-based views with few lines.
# This is where OOP comes into impact.

# Difference and advantages compared to function-based views:
# Code related to specific HTTP methods(GET,POST,etc.) can be addressed by separate methods instead of conditional branching.
# Object-oriented techniques such as multiple inheritance can be used to factor code into reusable components.


# views.py:

# An easy way to set those simple views that is called generic views.
# Unlike classic views, generic views are classes not functions.
# A set of classes for generic views in django.views.generic.
# Every generic view is one of those classes or a class that inherits from one of them.
'''
from django.views.generic import PythonView

class DjangoView(PythonView):
    template = "python.html"
'''

# urls.py:
'''
from django.urls import path
from app.views import DjangoView

urlpatterns = [
    path('data/',DjangoView.as_view()),
]
'''