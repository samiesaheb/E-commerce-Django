from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Order

@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "core/order_detail.html", {"order": order})
