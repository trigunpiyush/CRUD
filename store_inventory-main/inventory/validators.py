from django.core.exceptions import ValidationError
from django.db.models import Avg
from django.utils import timezone
from .models import CuboidBox
from django.conf import settings

def validate_average_area():
    max_average_area = settings.BOX_AVERAGE_AREA_LIMIT
    average_area = CuboidBox.objects.aggregate(Avg('area'))['area__avg']
    if average_area is not None and average_area > max_average_area:
        raise ValidationError("Average area exceeds the limit.")

def validate_user_average_volume(user):
    max_average_volume = settings.USER_AVERAGE_VOLUME_LIMIT
    average_volume = CuboidBox.objects.filter(creator=user).aggregate(Avg('volume'))['volume__avg']
    if average_volume is not None and average_volume > max_average_volume:
        raise ValidationError("Average volume exceeds the limit for the user.")

def validate_weekly_box_limit():
    max_weekly_limit = settings.WEEKLY_BOX_LIMIT
    current_week_start = timezone.now() - timezone.timedelta(days=timezone.now().weekday())
    box_count = CuboidBox.objects.filter(created_at__gte=current_week_start).count()
    if box_count > max_weekly_limit:
        raise ValidationError("Weekly box limit exceeded.")

def validate_weekly_user_box_limit(user):
    max_weekly_user_limit = settings.WEEKLY_USER_BOX_LIMIT
    current_week_start = timezone.now() - timezone.timedelta(days=timezone.now().weekday())
    box_count = CuboidBox.objects.filter(creator=user, created_at__gte=current_week_start).count()
    if box_count > max_weekly_user_limit:
        raise ValidationError("Weekly box limit exceeded for the user.")
