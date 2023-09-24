from django.db import models
from users.models import CustomUser

# Create your models here.

class Forum(models.Model):
    def __str__(self):
        return (f"{self.name}  #{str(self.id)}" )
    name = models.CharField(max_length=150)
    about = models.TextField()
    users = models.ManyToManyField(CustomUser,related_name='forums')
    mods = models.ManyToManyField(CustomUser,related_name='mod_forums')
    is_public = models.BooleanField(default=False)
    pic = models.ImageField(upload_to='forums', default='/forums/Dragonfruit2.jpg')
    
    
    

class Events(models.Model):
    def __str__(self):
        return(f"{self.title}  #{str(self.id)}")
    forum = models.ManyToManyField(Forum,related_name='events',blank=True)
    title = models.CharField(max_length=150)
    about = models.TextField()
    date = models.DateTimeField()
    is_public = models.BooleanField(default=False)
    users_added = models.ManyToManyField(CustomUser,blank=True,related_name='events_added')

    
class Notices(models.Model):
    def __str__(self):
        return(f"{self.title}  #{str(self.id)}")
    forum = models.ManyToManyField(Forum,related_name='notices')
    title = models.CharField(max_length=150)
    about = models.TextField()
    
    
class JoinReq(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
