import uuid
from django.db import models
from django.conf import settings


class ReceiveTransaction(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True
        )

    user_account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transaction_sent'
        )


    receive_value = models.DecimalField(
        max_digits=10,
        decimal_places=2
        )
    
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transaction_receive'
    )

    transaction_date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.receiver.username
    
    class Meta:
        ordering = ['-transaction_date']