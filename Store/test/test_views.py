from django.test import TestCase, Client
from django.urls import reverse
from Store.models import Order
from Store.connection import Connection
import json

class TestViews(TestCase):

    def setUp(self):

        self.client = Client()
        self.new_order_url = reverse("new_order")
        self.order_summary_url = reverse("order_summary", args=[1])
        self.payment_status_url = reverse("payment_status", args=[1])
        self.all_orders_url = reverse("all_orders")
        self.summary_payment_url = reverse("summary_payment", args=[1])
        self.try_new_payment_url = reverse("try_new_payment", args=[1])

        self.order1 = Order.objects.create(
            costumer_name = "Name1",
            costumer_email = "email1@email.com",
            costumer_mobile = "3011234562"
        )

    # GET tests

    def test_new_order_get(self):

        response = self.client.get(self.new_order_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "Store/new_order.html")

    def test_order_summary_get(self):

        response = self.client.get(self.order_summary_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "Store/order_summary.html")

    def test_payment_status_get(self):

        response = self.client.get(self.payment_status_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "Store/payment_status.html")

    def test_all_orders_get(self):

        response = self.client.get(self.all_orders_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "Store/all_orders.html")

    # POST tests

    def test_new_order_post_adds_new_order(self):
        
        order2Json = {
            "costumer_name": "Name2",
            "costumer_email": "email2@email.com",
            "costumer_mobile": "3001234567"
        }

        response = self.client.post(self.new_order_url, order2Json)
        order2 = Order.objects.get(id=2)
        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(order2.costumer_name, "Name2")


    def test_order_summary_post_new_payment(self):

        response = self.client.post(self.order_summary_url)

        self.assertEquals(response.status_code, 200)
        
    
    def test_new_payment(self):

        connection1 = Connection()

        response = connection1.make_payment(
            self.order1.id,
            self.order1.costumer_name,
            self.order1.costumer_email,
            self.order1.costumer_mobile
        )

        self.assertEquals(response.status_code, 200)
