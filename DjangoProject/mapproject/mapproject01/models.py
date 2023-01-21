from django.db import models

# Create your models here.
class Marker(users.Users):
    idusers.IntegerField(primary_key=True)
    nameusers.charfield(max_length=200)
    mailusers.charfield(max_length=200)
    passwordusers.charfield(max_length=200)

   