from django.dispatch import receiver
from django.contrib.auth.models import Group
from registration.signals import user_registered


@receiver(user_registered)
def user_registered_callback(sender, user, request, **kwargs):
    group_name = request.POST['group_id'] or None
    if group_name:
        try:
            g = Group.objects.get(name=group_name)
        except Group.DoewNotExists:
            g = None

        if g:
            g.user_set.add(user)