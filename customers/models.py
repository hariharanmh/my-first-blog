from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from shops.models import Shop
from .utils import unique_slug_generator
from .validators import validate_phone_number

User = settings.AUTH_USER_MODEL

class CustomerManager(models.Manager):
	def get_queryset(self):
		return CustomerQuerySet(self.model, using=self._db)
	
	def search(self, query):
		return self.get_queryset().search(query)


class CustomerQuerySet(models.query.QuerySet):
	
	def search(self, query):
		if query:
			query = query.strip()
			return self.filter(
				Q(customer_name__icontains=query) | Q(customer_name__iexact=query) |
				Q(customer_phone_number__icontains=query) | Q(customer_phone_number__iexact=query)
				).distinct()
		return self

class Customer(models.Model):
	user_id                     = models.ForeignKey(User)
	shop_id                     = models.ForeignKey(Shop, on_delete=models.CASCADE)
	customer_name               = models.CharField('Name', max_length=128)
	customer_phone_number       = models.CharField('Phone Number', max_length=16, validators=[validate_phone_number])
	customer_email_id           = models.EmailField('Email Id', max_length=256, null=True, blank=True)
	customer_sale_quantity      = models.IntegerField('Sale Quantity')
	customer_sale_quantity_desc = models.TextField('Sale Description',null=True, blank=True)
	customer_sale_price         = models.DecimalField('Price', max_digits=10,decimal_places=2) 
	date_of_entry               = models.DateTimeField(auto_now_add=True)
	date_of_update              = models.DateTimeField(auto_now=True)
	status                      = models.BooleanField(default=True)
	slug                        = models.SlugField(null=True, blank=True)

	# class Meta:
	# 	unique_together = ('shop_id', 'customer_phone_number')

	# def validate_unique(self, *args, **kwargs):
	# 	shop_id = Shop.objects.filter(shop_user_id=self.request.user).first()
	# 	if Customer.objects.filter(shop_id, customer_phone_number=self.customer_phone_number).exists():
	# 		raise ValidationError('Phone Number Alredy Exists')
	# 	super(Customer, self).validate_unique(*args, **kwargs)

	objects = CustomerManager()

	def __str__(self):
		return self.customer_name

	def get_absolute_url(self):
		return reverse('customers:detail', kwargs={'slug':self.slug})
	
	def get_absolute_url_update(self):
		return reverse('customers:update', kwargs={'slug':self.slug})

	def get_absolute_url_delete(self):
		return reverse('customers:delete', kwargs={'slug':self.slug})

	@property
	def title(self):
		return self.customer_name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Customer)