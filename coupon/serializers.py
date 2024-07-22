
from rest_framework import serializers
from .models import Coupon
from account.models import User

class CouponSerializer(serializers.ModelSerializer):
	user_id =  serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='user')
	
	class Meta:
		model = Coupon
		depth = 1
		fields = '__all__'