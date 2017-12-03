from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
# Create your models here.

class Blogger(models.Model):
  """
  Model representing a Blogger
  """
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  psuedo_name = models.CharField(max_length=100)
  email_id = models.EmailField()

  def __str__(self):
    return '%s, %s' % (self.last_name, self.first_name)

class Blog(models.Model):
  """
  Model representing a blog
  """
  title = models.CharField(max_length=200)
  blogger = models.ForeignKey(Blogger,on_delete = models.SET_NULL, null = True)
  content = models.TextField(blank=True)
  created_on = models.DateTimeField(auto_now=True) #auto_now got updated on each edit, auto_now_add on creation only
  topics = models.ManyToManyField('Topic')
  # comment = models.OneToOneField('Comment',on_delete=models.CASCASE,null=True,blank=True)
  
  class Meta:
    ordering = ["-created_on"]
  
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('blog-detail', args=[str(self.id)])


class Comment(models.Model):
  """
  Comment model
  """
  comment = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  blog = models.OneToOneField(Blog)
  user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='commenter',default=1)
  
  def __str__(self):
    return " %s (%s)" %(self.comment[:10], self.user)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created = False, **kwargs):
  if created:
    Token.objects.create(user=instance)

class Topic (models.Model):
  topic = models.CharField(max_length=50)
  
  def __str__(self):
    return self.topic