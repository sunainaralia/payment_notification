from django.db import models
from django.contrib.auth.models import User


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField()
    payment_status = models.CharField(
        max_length=50,
        choices=[("Pending", "Pending"), ("Partial", "Partial"), ("Paid", "Paid")],
    )
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    notification_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.payment_status} - {self.due_date}"
