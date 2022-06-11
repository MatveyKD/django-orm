from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import django

import datetime


def storage_information_view(request):
    non_closed_visits_info = []

    active_passcards = Passcard.objects.filter(is_active=True)

    non_closed_visits = Visit.objects.filter(leaved_at=None)
    for visit in non_closed_visits:
        located_time = visit.get_duration()
        seconds = located_time.total_seconds()
        hours = int(seconds // 3600)
        minutes = int(seconds % 3600 // 60)
        time_inside = f"{hours}:{minutes}"
        name = visit.passcard.owner_name
        non_closed_visits_info.append({
            'who_entered': name,
            'entered_at': visit.entered_at,
            'duration': time_inside
        })

    context = {
        'non_closed_visits': non_closed_visits_info,
    }
    return render(request, 'storage_information.html', context)
