from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from .utils import unique_slug_generator
from .validators import validate_phone_number

User = settings.AUTH_USER_MODEL

class Shop(models.Model):
	shop_user_id      = models.ForeignKey(User)
	shop_name         = models.CharField('Shop Name', max_length=128)
	shop_phone_number = models.CharField('Phone Number',max_length=16, unique=True, validators=[validate_phone_number])
	shop_city         = models.CharField('City', max_length=128)
	shop_address      = models.TextField('Address', null=True, blank=True)
	shop_category     = models.CharField('Shop Category', max_length=128, null=True, blank=True)
	shop_type         = models.CharField('Shop Type', max_length=128, null=True, blank=True)
	date_of_entry     = models.DateTimeField(auto_now_add=True)
	date_of_update    = models.DateTimeField(auto_now=True)
	status            = models.BooleanField(default=True)
	slug              = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.shop_name

	def get_absolute_url(self):
		return reverse('shops:detail', kwargs={'slug':self.slug})

	def get_absolute_url_update(self):
		return reverse('shops:update', kwargs={'slug':self.slug})

	@property
	def title(self):
		return self.shop_name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Shop)