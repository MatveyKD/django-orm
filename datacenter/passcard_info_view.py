from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    this_passcard_visits = []

    visits = Visit.objects.filter(passcard=passcard)
    for visit in visits:
        visit_duration = visit.get_duration()
        hours = visit_duration.total_seconds() // 3600
        minutes = visit_duration.total_seconds() // 60
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': f'{hours}:{minutes}',
            'is_strange': visit.is_long()
        })
    print(this_passcard_visits)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
