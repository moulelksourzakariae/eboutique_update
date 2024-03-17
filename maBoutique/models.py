from django.db import models
from django.contrib.auth.models import User
class Article(models.Model):
    titre = models.CharField(max_length=150)
    description = models.TextField()
    def str(self):
        return self.titre
