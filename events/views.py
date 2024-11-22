from django.shortcuts import render, redirect

from .models import Event, Participant

# Create your views here.
# def add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         location = request.POST.get('location')
#         start_time = request.POST.get('start_time')
#         end_time = request.POST.get('end_time')
#         organizer = request.POST.get('organizer')
#
#         data = Event.objects.all()
#         context =  {"data": data}
#
#         query = Event(name=name, description=description, location=location, start_time=start_time, end_time=end_time, organizer=organizer)
#         query.save()
#         return render(request, 'add_events.html', context)
#     return render(request, 'add_events.html')

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        location = request.POST.get('location')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        organizer = request.POST.get('organizer')

        # Save the new event
        Event.objects.create(
            name=name,
            description=description,
            location=location,
            start_time=start_time,
            end_time=end_time,
            organizer=organizer
        )

    # Fetch all events to display in the table
    data = Event.objects.all()
    context = {"data": data}
    return render(request, 'add_events.html', context)


def events(request):
    event = Event.objects.all()
    context = {"event": event}
    return render(request, 'events.html', context)

# def update_event(request, id):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         location = request.POST.get('location')
#         start_time = request.POST.get('start_time')
#         end_time = request.POST.get('end_time')
#         organizer = request.POST.get('organizer')
#         edit = Event.objects.get(id=id)
#         edit.name = name
#         edit.description = description
#         edit.location = location
#         edit.start_time = start_time
#         edit.end_time = end_time
#         edit.organizer = organizer
#         edit.save()
#         return redirect('/event/')
#
#     d = Event.objects.get(id=id)
#     context = {'d': d}
#     return render(request, 'update_event.html', context)

def update_event(request, id):
    try:
        edit = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return redirect('event')  # Redirect if the event doesn't exist.

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        location = request.POST.get('location')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        organizer = request.POST.get('organizer')

        # Validate data
        if all([name, description, location, start_time, end_time, organizer]):
            edit.name = name
            edit.description = description
            edit.location = location
            edit.start_time = start_time
            edit.end_time = end_time
            edit.organizer = organizer
            edit.save()
            return redirect('event')

    context = {'d': edit}
    return render(request, 'update_event.html', context)


def delete_event(request, id):
    d = Event.objects.get(id=id)
    d.delete()
    return redirect('/event/')

def participants(request):
    participant = Participant.objects.all()
    context = {"participant": participant}
    return render(request, 'participants.html', context)

# def participants(request):
#     participant = Participant.objects.prefetch_related('events').all()  # Prefetch to optimize queries.
#     context = {"participant": participant}
#     return render(request, 'participants.html', context)


# def add_participant(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         events = request.POST.get('events')
#
#         data = Participant.objects.all()
#         context =  {"data": data}
#
#         query = Participant(name=name, email=email, events=events)
#         query.save()
#         return render(request, 'add_participant.html', context)
#     return render(request, 'add_participant.html')
def add_participant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        events_ids = request.POST.getlist('events')  # Use `getlist` to capture multiple event IDs.

        participant = Participant(name=name, email=email)
        participant.save()  # Save the participant first to create the instance.

        # Add events to the participant using `add`.
        if events_ids:
            events = Event.objects.filter(id__in=events_ids)
            participant.events.add(*events)

        return redirect('participants')  # Redirect to participants list or any desired page.

    events = Event.objects.all()  # Fetch all events for selection in the form.
    context = {'events': events}
    return render(request, 'add_participant.html', context)


# def update_participant(request, id):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         events = request.POST.get('events')
#
#         edit = Participant.objects.get(id=id)
#         edit.name = name
#         edit.email = email
#         edit.events = events
#         edit.save()
#         return redirect('/participant/')
#
#     d = Participant.objects.get(id=id)
#     context = {'d': d}
#     return render(request, 'update_participants.html', context)

def update_participant(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        events_ids = request.POST.getlist('events')  # Capture multiple event IDs.

        edit = Participant.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.save()  # Save the changes to the participant.

        # Update the participant's events.
        events = Event.objects.filter(id__in=events_ids)
        edit.events.set(events)

        return redirect('participants')  # Redirect to the participants list.

    d = Participant.objects.get(id=id)
    events = Event.objects.all()  # Fetch all events for display in the form.
    context = {'d': d, 'events': events}
    return render(request, 'update_participants.html', context)


def delete_participant(request, id):
    d = Participant.objects.get(id=id)
    d.delete()
    return redirect('event')