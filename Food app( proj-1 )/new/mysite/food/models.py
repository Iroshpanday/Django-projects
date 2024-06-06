from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name
    # yo def_str wala line lah chai BD batsa jaba hamla k k xa vanra herna khojxau taba item ko name nai display gardinxa 
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default=" https://imgs.search.brave.com/DfARh4xce92UG7isvTGb8bf9TzobcfH3Z3Sbo8oy-24/rs:fit:860:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzA3LzYxLzM5LzE4/LzM2MF9GXzc2MTM5/MTg1M19aWWZCc0V1/NDREZlJ1Wk5JaDJH/NVh2UVBkSExoTGZq/MS5qcGc")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
  