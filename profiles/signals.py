from random import choice

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

from profiles.models import User, Profile

from clans.models import Clan


# @property
def get_clan():
    clan_quantity: int = Clan.objects.count()

    try:
        average_num_of_users_per_clan: int = round(User.objects.count() / clan_quantity)
    except ZeroDivisionError:
        return

    # average_num_of_users_per_clan: int = round(User.objects.count() / clan_quantity)

    clans: list = Clan.objects.all()

    relatively_free_clans = []

    for i in range(clan_quantity):

        if clans[i].profiles.count() > average_num_of_users_per_clan:
            continue
        else:
            relatively_free_clans.append(clans[i])

    return choice(relatively_free_clans)


@receiver(post_save, sender=User)
def auto_profile_create(
    sender, instance, created, **kwargs
):
    if created:
        get_clan()

        print('Signal received!')
        Profile.objects.create(
            user=instance,
            clan=get_clan()
        )
        print('Profile created')
