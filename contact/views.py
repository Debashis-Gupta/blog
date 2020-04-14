from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.firstname=request.POST.get('firstname')
        contact.lastname=request.POST.get('lastname')
        contact.phone=request.POST.get('phone')
        contact.email=request.POST.get('email')
        contact.message=request.POST.get('message')
        contact.save()
        return redirect("home")
    else:
        return render(request,'contact.html',{})


def message(request):
    return render(request,'message.html',{})