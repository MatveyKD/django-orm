from django.db import models
import datetime
import django


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def is_long(self, minutes=60):
        return get_duration(self).total_seconds() > minutes * 60

    def get_duration(self):
        return get_duration(self)


def get_duration(visit):
    now = datetime.datetime.now().astimezone()

    entered_at = django.utils.timezone.localtime(visit.entered_at)
    if visit.leaved_at:
        duration = visit.leaved_at-entered_at
    else:
        duration = now-entered_at

    return duration
