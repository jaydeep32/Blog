from django.db import models
from django.conf import settings
from blog.models import Post


User = settings.AUTH_USER_MODEL

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    image = models.ImageField(upload_to='comment', default='author-3.jpg')
    created_at = models.DateTimeField(auto_now=True)

    @property
    def get_fullname(self):
        print(self.user.get_full_name)
        return self.user.get_full_name()

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"


class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replycomments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='comment', default='author-3.jpg')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"



