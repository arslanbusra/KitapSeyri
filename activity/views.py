from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Participant, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    participants = Participant.objects.filter(event=event)
    comments = Comment.objects.filter(event=event)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.event = event
            comment.save()
            return redirect('event_detail', pk=pk)
    else:
        comment_form = CommentForm()
    return render(request, 'events/event_detail.html', {
        'event': event,
        'participants': participants,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def join_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    Participant.objects.get_or_create(user=request.user, event=event)
    return redirect('event_detail', pk=pk)


