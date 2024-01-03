from django.db import models


class ServiceFeedbackModel(models.Model):
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="timestamp of creation order feedback"
        )
    submited_by = models.EmailField(max_length=255)

    def __repr__(self):     # same as __str__(self):
        return "{}".format(self.id)
