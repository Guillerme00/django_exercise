from django.views import generic
from django.shortcuts import render
from payment.models.ReceiveTransaction import ReceiveTransaction


class HomeView(generic.ListView):
    model = ReceiveTransaction
    template_name = 'index.html'
    ordering = ['-id']
    context_object_name = 'receives'

class PaymentDetail(generic.DetailView):
    model = ReceiveTransaction
    template_name = 'post_detail.html'
    context_object_name = 'receive'

def receive_list(request):
    receives = ReceiveTransaction.objects.all()
    return render(request, "payment/receive_list.html", {
        "receives": receives
    })