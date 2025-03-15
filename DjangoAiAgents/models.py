from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):
    name = models.CharField(max_length=100)
    api_url = models.URLField()
    api_key = models.CharField(max_length=255)
    app_id = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Dialog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    prompt = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.agent}"