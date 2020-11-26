from django.db import models
from django.conf import settings
  

class Article(models.Model):
  title = models.CharField(max_length=100)
  category = models.IntegerField()
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="article_user")
  username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field="username", related_name="article_username")
  

  def __str__(self):
    return self.content


class Comment(models.Model):
  content = models.TextField()
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_user")
  username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field="username", related_name="comment_username")

  def __str__(self):
    return self.content
