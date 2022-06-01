from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import django

import datetime


def get_duration(visit):
    now = datetime.datetime.now().astimezone()

    entered_at = django.utils.timezone.localtime(visit.entered_at)
    if visit.leaved_at:
        located_time = visit.leaved_at-entered_at
    else:
        located_time = now-entered_at
    seconds = located_time.total_seconds()
    hours = int(seconds // 3600)
    minutes = int(seconds % 3600 // 60)
    time_inside = f"{hours}:{minutes}"
    return located_time


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > 3600


def storage_information_view(request):
    non_closed_visits = []

    active_passcards = Passcard.objects.filter(is_active=True)
    now = datetime.datetime.now().astimezone()

    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        entered_at = django.utils.timezone.localtime(visit.entered_at)
        located_time = now-entered_at
        seconds = located_time.total_seconds()
        hours = int(seconds // 3600)
        minutes = int(seconds % 3600 // 60)
        time_inside = f"{hours}:{minutes}"
        name = visit.passcard.owner_name
        non_closed_visits.append({
            'who_entered': name,
            'entered_at': entered_at,
            'duration': time_inside
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
