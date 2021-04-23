from django.shortcuts import render, redirect
from .forms import Order_form
from .models import Order
from .connection import Connection


def new_order_view(request):

    """ 
    This view shows the form that captures the customer information to request
    the payment. 
    """

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

def payment(request, id):

    """
    This function creates a connection object and uses it to request a payment 
    session by sending the customer's information to PlaceToPay's Web-checkout service.
    And save de response data in the order table.
    """

    order = Order.objects.get(id=id)
    connection = Connection()
    response = connection.make_payment(
        order.id, order.costumer_name, order.costumer_email, order.costumer_mobile
    ).json()
    
    order.request_id = response["requestId"]
    order.process_url = response["processUrl"]
    order.save()

    return redirect(response["processUrl"])
