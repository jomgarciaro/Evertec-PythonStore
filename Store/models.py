from django.db import models

class Order(models.Model):
    costumer_name = models.CharField("Name", max_length=80)
    costumer_email = models.EmailField("Email", max_length=120)
    costumer_mobile = models.CharField("Mobile", max_length=40)
    status = models.CharField("Status", max_length=20, default="CREATED")
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
   
