
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Payment


class PaymentNotifications(APIView):
    def get(self, request):
        payments = Payment.objects.filter(user=request.user)
        data = [
            {
                "due_date": payment.due_date,
                "status": payment.payment_status,
                "amount_due": payment.amount_due,
            }
            for payment in payments
        ]
        return Response({"payments": data})
