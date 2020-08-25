from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})
    #return HttpResponse("<h1>{} Stop trying to hack us!<>".format(request.user))

def contact_view(request,*args, **kwargs):
    #return HttpResponse("<h1>Contact Page<h1>")
    return render(request, "contact.html", {})

def about_view(request,*args, **kwargs):
    #return HttpResponse("<h1>About<h1>")
    my_context = {
    	"my_text": "This is about us",
    	"my_number": 123,
    	"my_list": [121, 25, 66885, 2001]
    }
   # my_list2 = [121, 25, 66885, 2001]
    return render(request, "about.html", my_context)

def social_view(request,*args, **kwargs):
    #return HttpResponse("<h1>Social Media<h1>")
    return render(request, "social.html", {})