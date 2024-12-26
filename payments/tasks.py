from celery import shared_task
from django.utils.timezone import now
from .models import Payment
from .utils import send_notification
from datetime import timedelta


@shared_task
def send_due_payment_notifications():
    payments = Payment.objects.filter(
        due_date=now().date() + timedelta(days=1),
        payment_status="Pending",
        notification_sent=False,
    )
    for payment in payments:
        message = (
            f"Ciao! La tua rata per la NFS ACADEMY è in scadenza domani, come di consueto sarà "
            "trattenuta la cifra concordata dal tuo conto corrente."
        )
        send_notification(payment.user.profile.phone_number, message)
        payment.notification_sent = True
        payment.save()


@shared_task
def send_overdue_payment_notifications():
    payments = Payment.objects.filter(
        due_date__lt=now().date() - timedelta(days=10),
        payment_status__in=["Pending", "Partial"],
    )
    for payment in payments:
        message = (
            f"Ciao! La tua rata per la NFS ACADEMY è scaduta il {payment.due_date}, ricordati di saldarla "
            "mezzo bonifico bancario al seguente IBAN: IT45X0623001614000015369315."
        )
        send_notification(payment.user.profile.phone_number, message)
