from django.db import models

class Conversation(models.Model):
    user_input = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Conversation {self.id} - {self.timestamp}"