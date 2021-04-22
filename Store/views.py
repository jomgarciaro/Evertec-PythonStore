from django.shortcuts import render, redirect
from .forms import Order_form
from .models import Order

def new_order_view(request):

    if request.method == "POST":
        form = Order_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(order_summary_view, id=form.save().id)
    else:
        form = Order_form()

    context = {"form": form}

    return render(request, "tienda/new_order.html", context)

def order_summary_view(request, id):

    order = Order.objects.get(id=id)
    context = {"order": order}

    return render(request, "tienda/order_summary.html", context)
