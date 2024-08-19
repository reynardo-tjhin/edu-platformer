from django.db import models

# Create your models here.
class Player(models.Model):
    # stores the uuid of the player
    player_id = models.CharField(max_length=32)

    # store the name and password
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=64) # using sha256 algorithm of hashlib

    # store the other descriptions for the game
    current_level = models.IntegerField()