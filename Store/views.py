from django.shortcuts import render, redirect
from .forms import Order_form
from .models import Order


def new_order_view(request):

    """ This view shows the form that captures the customer information. """

    if request.method == "POST":
        form = Order_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(order_summary_view, id=form.save().id)
    else:
        form = Order_form()

    context = {"form": form}

    return render(request, "Store/new_order.html", context)


def order_summary_view(request, id):

    """
    This view displays the customer's purchase order information and 
    allows the customer to go to Placetopay to make the payment.
    """

    order = Order.objects.get(id=id)
    context = {"order": order}

    return render(request, "Store/order_summary.html", context)
