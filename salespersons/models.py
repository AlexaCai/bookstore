from django.db import models
from django.contrib.auth.models import User # needed for OneToOneField


# Create your models here.

class Salesperson (models.Model):
    # 'CASCADE' specifies that whenever the user with username is deleted, the complete profile of the \
    # salesperson will be also deleted.
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    bio = models.TextField(default="no bio...")
    pic = models.ImageField(upload_to='salespersons', default='no_picture.jpg')


    def __str__(self):
	    return f"Profile of {self.name}"
		# f-string allows to format the string, so for username abc, you will see: Profile of abc 