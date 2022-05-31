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
    print("Находится", time_inside)
    return located_time
    #name = visit.passcard.owner_name
    #non_closed_visits.append({
        #'who_entered': name,
        #'entered_at': entered_at,
        #'duration': time_inside
    #})

def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    print(duration)
    return duration.total_seconds() > 3600
def storage_information_view(request):
    non_closed_visits = []
    
    # Программируем здесь
    active_passcards = Passcard.objects.filter(is_active=True)
    now = datetime.datetime.now().astimezone()
    print(now)

    visits = Visit.objects.filter(leaved_at=None)
    print(visits)
    for visit in visits:
        print(is_visit_long(visit))
        entered_at = django.utils.timezone.localtime(visit.entered_at)
        located_time = now-entered_at
        seconds = located_time.total_seconds()
        hours = int(seconds // 3600)
        minutes = int(seconds % 3600 // 60)
        #seconds = int(seconds % 3600 // 60 // 60)
        time_inside = f"{hours}:{minutes}"
        #print("Находится", time_inside)
        name = visit.passcard.owner_name
        non_closed_visits.append({
            'who_entered': name,
            'entered_at': entered_at,
            'duration': time_inside
        })
    print(non_closed_visits)


    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
