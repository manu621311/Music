from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from .models import music,event
from django.views.generic import ListView
from hitcount.views import HitCountDetailView###new


# Create your views here.
def home(request):
    Music = music.objects.all()
    return render(request,'index.html',{'music':Music});


def about(request):
    return render(request,'about.html');

def emailview(request):
    if request.method =="POST":
        your_name=request.POST.get('name')
        your_contact=request.POST.get('contact')
        your_email=request.POST.get('Email')
        your_location=request.POST.get('Location')
        your_date=request.POST.get('Date')
        your_message=request.POST.get('message')
        booking="name:\n" + str(your_name) +"\n\ncontact:\n"+ str(your_contact) +"\n\nemail:\n"+ str(your_email) + "\n\nlocation:\n" + str(your_location) +"\n\nDate:\n"+ str(your_date) + "\n\nmessage:\n"+ str(your_message)
        email=EmailMessage(
          'Booking request',
           booking,
          to=['sagartyagi526@gmail.com'],
          )
        email.send()
        return redirect('/')
    return render(request,'contact.html');
def mix(request):
    Music = music.objects.all()
    return render(request,'track.html',{'music':Music});
def events(request):
    Events = event.objects.all()
    return render(request,'blog.html',{'event':Events})

def contact(request):
    return render(request,'contact.html')
def eventdetail(request,id):
    Event=event.objects.get(id=id)
    return render(request,'detailblog.html',{'event':Event});  
class Download(HitCountDetailView):#new
    model=music
    template_name='download_page.html'
    count_hit=True
    context_object_name='music'    
