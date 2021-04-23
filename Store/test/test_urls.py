from django.test import SimpleTestCase
from django.urls import resolve, reverse
from Store.views import new_order_view, payment_status_view, order_summary_view, all_orders_view, payment

class TestUrls(SimpleTestCase):

    def test_new_order_url_resolves(self):
        url = reverse('new_order')
        self.assertEquals(resolve(url).func, new_order_view)

    def test_order_status_url_resolves(self):
        url = reverse('payment_status', args=[0])
        self.assertEquals(resolve(url).func, payment_status_view)

    def test_order_summary_url_resolves(self):
        url = reverse('order_summary', args=[0])
        self.assertEquals(resolve(url).func, order_summary_view)

    def test_all_orders_url_resolves(self):
        url = reverse('all_orders')
        self.assertEquals(resolve(url).func, all_orders_view)

    def test_summary_payment_url_resolves(self):
        url = reverse('summary_payment', args=[0])
        self.assertEquals(resolve(url).func, payment)

    def test_payment_status_url_resolves(self):
        url = reverse('try_new_payment', args=[0])
        self.assertEquals(resolve(url).func, payment)




    
