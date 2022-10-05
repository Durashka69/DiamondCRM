# from random import choice

# from django.dispatch import receiver
# from django.db.models.signals import m2m_changed, post_save

# from clans.models import User, Clan

# from profiles.models import Profile


# @receiver(post_save, sender=User)
# def auto_user_save_to_Clan(sender, instance, created, **kwargs):
#     if created:
#         print('signal received!')
#         clan_quantity = Clan.objects.count()
#         average_users_per_clan = round(User.objects.count() / clan_quantity)

#         clans = Clan.objects.all()

#         for clan in clans:
#             if clan.users.count():
#                 pass