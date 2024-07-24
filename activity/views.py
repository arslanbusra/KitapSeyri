from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Participant
from django.contrib.auth.decorators import login_required

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    participants = Participant.objects.filter(event=event)
    return render(request, 'events/event_detail.html', {'event': event, 'participants': participants})

@login_required
def join_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    Participant.objects.get_or_create(user=request.user, event=event)
    return redirect('event_detail', pk=pk)

