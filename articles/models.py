from django.conf import settings
from django.db import models
from django.urls import reverse

import openai
#from api_secrets import OPENAI_API_KEY

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    phrase = models.TextField(null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


class Comment(models.Model): # new
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_list")


class aiw:
   def __init__(self):
      self.val=1      
      openai.api_key = os.getenv("OPENAI_API_KEY")
      openai.Model.list()
      self.prompt = "hello worlds"

   def getVal(self):
      return self.val*self.val

   def __str__(self):
      return self.prompt
