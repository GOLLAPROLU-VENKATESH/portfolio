from django.urls import path
from .views import home,projects,resume,aboutme,Contact

urlpatterns = [
    path('',home,name='home'),
    path('projects',projects, name='projects'),
    path('resume',resume,name='resume'),
    path('aboutme',aboutme , name='aboutme'),
    path('contact', Contact.as_view(), name='contact')
]