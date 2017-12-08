from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Shop
from .forms import ShopModelForm, RegisterModelForm

class ShopListView(LoginRequiredMixin,ListView):
	def get_queryset(self):
		return Shop.objects.filter(shop_user_id=self.request.user)

class ShopDetailView(LoginRequiredMixin, DetailView):

	def get_queryset(self):
		return Shop.objects.filter(shop_user_id=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context          = super(ShopDetailView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Shop Detail'
		return context


class ShopCreateView(LoginRequiredMixin, CreateView):
	form_class      = ShopModelForm
	template_name   = 'form.html'
	success_url     = '/shops/'
	success_message = 'Shop Created Successfully'

	def get(self, request):
		qs_exist = Shop.objects.filter(shop_user_id=self.request.user).exists()
		if qs_exist:
			return HttpResponseRedirect('/customers/')
		return super(ShopCreateView, self).get(request) 	

	def get_queryset(self):
		return Shop.objects.filter(shop_user_id=self.request.user)

	def form_valid(self, form):
		obj               = form.save(commit=False)
		obj.shop_user_id  = self.request.user
		return super(ShopCreateView, self).form_valid(form)

	# def get_form_kwargs(self):
	# 	kwargs                 = super(ShopCreateView, self).get_form_kwargs()
	# 	kwargs['shop_user_id'] = self.request.user
	# 	return kwargs

	def get_context_data(self, *args, **kwargs):
		context          = super(ShopCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Create Store'
		return context

class ShopUpdateView(LoginRequiredMixin, UpdateView):
	form_class    = ShopModelForm
	template_name = 'form.html'
	success_url     = '/shops/'
	success_message = 'Shop Updated Successfully'
	# success_url     = '/shops/{slug}/'

	def get_queryset(self):
		return Shop.objects.filter(shop_user_id=self.request.user)

	def form_valid(self, form):
		obj          = form.save(commit=False)
		obj.user_id  = self.request.user
		obj.shop_id = Shop.objects.filter(shop_user_id=self.request.user).first()
		return super(ShopUpdateView, self).form_valid(form)

	# def get_form_kwargs(self):
	# 	kwargs                 = super(ShopUpdateView, self).get_form_kwargs()
	# 	kwargs['shop_user_id'] = self.request.user
	# 	return kwargs

	def get_context_data(self, *args, **kwargs):
		context          = super(ShopUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Shop Customer'
		return context

class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterModelForm
    template_name = 'registration/register.html'
    success_url = '/logout/'
    success_message = "Your account was created successfully. Please check your email."

    def dispatch(self, *args, **kwargs):
        # if self.request.user.is_authenticated():
        #     return redirect("/logout")
        return super(RegisterView, self).dispatch(*args, **kwargs)
