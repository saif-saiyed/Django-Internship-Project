from django.urls import path
from home.views import index, aboutus, contactus

urlpatterns = [
    path('', index, name ="index"),
    path('aboutus', aboutus, name = "aboutus"),
    path('contactus', contactus, name = "contactus"),
    #path('userprofile', userprofile, name = "userprofile")    
]