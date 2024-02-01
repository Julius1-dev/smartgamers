from django.db import models
from users.models import CustomUsers


class Gamers(CustomUsers):
    gamer_tag=models.CharField(max_length=200)



