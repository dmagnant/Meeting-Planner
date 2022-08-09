from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from django.views.generic.edit import BaseCreateView

from .models import Meeting, Room
from .forms import MeetingForm

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def roomsList(request):
    return render(request, "meetings/roomsList.html", {"rooms": Room.objects.all()})

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:        
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})