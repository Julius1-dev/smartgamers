from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from users.models import CustomUsers

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUsers.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except CustomUsers.DoesNotExist:
            return None  # User not found, return None
        except CustomUsers.MultipleObjectsReturned:
            user = CustomUsers.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        else:
            return None  # Password didn't match, return None
