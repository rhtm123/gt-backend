from django.db import models

# Create your models here.

from account.models import User


class Coupon(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	code = models.CharField(max_length=20)
	discount = models.IntegerField()
	expire_date = models.DateTimeField()

	def __str__(self):
		return self.code
