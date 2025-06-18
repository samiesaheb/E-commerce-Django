from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from core.models import Order

@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # ✅ No need to manually assign `subtotal` anymore

    return render(request, "core/order_detail.html", {"order": order})
