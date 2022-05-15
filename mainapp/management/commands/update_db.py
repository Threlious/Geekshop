from django.core.management.base import BaseCommand
from authapp.models import ShopUserProfile, ShopUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = ShopUser.objects.all()
        for user in users:
            users_profile = ShopUserProfile.objects.create(user=user)
            users_profile.save()
