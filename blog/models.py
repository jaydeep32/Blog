from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


User = settings.AUTH_USER_MODEL

class Post(models.Model):
    image = models.ImageField(upload_to='blog')
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.title

@receiver(pre_save, sender=Post)
def saev_slug(sender, instance, *args, **kwargs):
    if instance.title:
        instance.slug = slugify(instance.title)