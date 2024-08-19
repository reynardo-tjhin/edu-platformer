from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Player(AbstractUser):
    # # stores the uuid of the player
    # player_id = models.CharField(max_length=32, unique=True)
    # USERNAME_FIELD = "player_id"
    # store the name and other descriptions for the game
    username = models.CharField(max_length=50, unique=True)
    current_level = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.username
