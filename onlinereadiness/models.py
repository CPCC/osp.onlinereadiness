from django.db import models
from django.contrib.auth.models import User

class OnlineReadinessResult(models.Model):
    """
        Stores students reponses to online readiness assessment.
    """
    student = models.ForeignKey(User)
    answers = models.TextField()
    date_taken = models.DateTimeField(auto_now_add=True)

