from django import forms
from shops.models import Shop
from .models import Customer

class CustomerModelForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = [
			'customer_phone_number', 
			'customer_name', 
			'customer_email_id', 
			'customer_sale_quantity', 
			'customer_sale_quantity_desc', 
			'customer_sale_price',
		]

	def  __init__(self, user_id=None, *args, **kwargs):
		# print(user_id)
		# print(kwargs)
		super(CustomerModelForm, self).__init__(*args, **kwargs)
		Customer.shop_id.queryset = Shop.objects.filter(shop_user_id=user_id)
		#print(Customer.shop_id.queryset)