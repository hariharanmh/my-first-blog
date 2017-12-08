import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db.models import Q, Sum, Count
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import datetime 
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.dates import TodayArchiveView, YearArchiveView
from msg91 import check_balance
from shops.models import Shop
from .models import Customer
from .forms import CustomerModelForm


class CustomerListView(LoginRequiredMixin, ListView):

	def  get(self, request):
		qs = Shop.objects.filter(shop_user_id=self.request.user)
		if not qs.exists():
			return HttpResponseRedirect('/shops/create/')
		return super(CustomerListView, self).get(request)

	def get_queryset(self):
		return Customer.objects.filter(user_id=self.request.user).order_by('-date_of_update')

	def get_context_data(self, *args, **kwargs):
		context              = super(CustomerListView, self).get_context_data(*args, **kwargs)
		context['title']     = 'Customer List' 
		context['shop']      = Shop.objects.filter(shop_user_id=self.request.user).values().first()
		return context

class CustomerDetailView(LoginRequiredMixin, DetailView):

	def get_queryset(self):
		return Customer.objects.filter(user_id=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context          = super(CustomerDetailView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Customer Detail'
		return context


class CustomerCreateView(LoginRequiredMixin, CreateView):
	form_class    = CustomerModelForm
	template_name = 'form.html'
	success_url   = '/customers/'
	
	def get_queryset(self):
		return Customer.objects.filter(user_id=self.request.user)

	def form_valid(self, form):
		obj          = form.save(commit=False)
		obj.user_id  = self.request.user
		obj.shop_id  = Shop.objects.filter(shop_user_id=self.request.user).first()
		return super(CustomerCreateView, self).form_valid(form)

	def get_form_kwargs(self):
		kwargs            = super(CustomerCreateView, self).get_form_kwargs()
		kwargs['user_id'] = self.request.user
		return kwargs

	def get_context_data(self, *args, **kwargs):
		context          = super(CustomerCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Customer'
		return context

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
	form_class    = CustomerModelForm
	template_name = 'form.html'
	success_url   = '/customers/'

	def get_queryset(self):
		return Customer.objects.filter(user_id=self.request.user)

	def form_valid(self, form):
		obj          = form.save(commit=False)
		obj.user_id  = self.request.user
		obj.shop_id  = Shop.objects.filter(shop_user_id=self.request.user).first()
		return super(CustomerUpdateView, self).form_valid(form)

	def get_form_kwargs(self):
		kwargs            = super(CustomerUpdateView, self).get_form_kwargs()
		kwargs['user_id'] = self.request.user
		return kwargs

	def get_context_data(self, *args, **kwargs):
		context          = super(CustomerUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Edit Customer'
		return context

class CustomerDeleteView(LoginRequiredMixin, DeleteView):
	model           = Customer
	success_url     = '/customers/'
	success_message = 'Deleted Successfully'

	def get_context_data(self, *args, **kwargs):
		context          = super(CustomerDeleteView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Delete Customer'
		return context

class CustomerTodayArchiveView(LoginRequiredMixin, TodayArchiveView):
	date_field   = "date_of_entry"
	allow_future = True

	def  get(self, request):
		qs       = Customer.objects.filter(user_id=self.request.user, date_of_entry__day=datetime.today().day)
		if not qs.exists():
			return HttpResponse("{%  extends 'super.html' %} No customers has been added Today")
		return super(CustomerTodayArchiveView, self).get(request)

	def get_queryset(self):
		return Customer.objects.filter(user_id=self.request.user)
	
	def get_context_data(self, *args, **kwargs):
		context                   = super(CustomerTodayArchiveView, self).get_context_data(*args, **kwargs)
		context['title']          = 'Today Customer List'
		qs       				  = Customer.objects.filter(user_id=self.request.user, date_of_entry__day=datetime.today().day)
		context['total_price']    = qs.aggregate(Sum('customer_sale_price'))
		context['total_quantity'] = qs.aggregate(Sum('customer_sale_quantity'))
		return context


class CustomerYearArchiveView(LoginRequiredMixin, YearArchiveView):
	date_field   = "date_of_entry"
	make_object_list = True
	allow_future = True

	def get_queryset(self):
		return Customer.objects.filter(user_id=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context                   = super(CustomerYearArchiveView, self).get_context_data(*args, **kwargs)
		context['title']          = 'Today Customer List'
		qs       				  = Customer.objects.filter(user_id=self.request.user, date_of_entry__year=datetime.today().year)
		context['total_price']    = qs.aggregate(Sum('customer_sale_price'))
		context['total_quantity'] = qs.aggregate(Sum('customer_sale_quantity'))
		return context



# class CustomerView(LoginRequiredMixin, View):
# 	def  get(self, request):
# 		query         = self.request.GET.get('query', None)
# 		search_list   = []
# 		if query:
# 			search_qs = Customer.objects.filter(user_id=self.request.user).search(query)
# 			for s in search_qs:
# 				name  = "%s" % (s.customer_name)
# 				search_dict = {
# 					"name"  : s.customer_name,
# 					"phone" : s.customer_phone_number,
# 				}
# 				search_list.append(search_dict)
# 			print(search_list)
# 			return HttpResponse(json.dumps(search_list), content_type='application/json')
# 		else :
# 			return HttpResponse(json.dumps(search_list), content_type='application/json')
# 		return super(CustomerListView, self).get(request)

# class CustomerTemplateView(TemplateView):
# 	template_name = 'customers/customer_search_list.html'

# 	def get_context_data(self, *args, **kwargs):
# 		context          = super(CustomerTemplateView, self).get_context_data(*args, **kwargs)
# 		context['title'] = 'Search List'
# 		query                = self.request.GET.get('query', None)
# 		if query:
# 			context['title']    = 'Search List'
# 			qs                  = Customer.objects.filter(user_id=self.request.user).search(query)
# 			context['customer'] = qs
# 			print(qs)
# 		return context