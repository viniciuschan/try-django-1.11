from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import (
	TemplateView,
	ListView,
	DetailView,
	CreateView,
)
from .forms import RestaurantLocationCreateForm
from .models import RestaurantLocation


class RestaurantListView(ListView):
	template_name = 'restaurants/restaurants_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
					Q(category__iexact=slug) |
					Q(category__icontains=slug)
				)
		else:
			queryset = RestaurantLocation.objects.all()

		return queryset


class RestaurantDetailView(DetailView):
	template_name = 'restaurants/restaurants_detail.html'
	queryset = RestaurantLocation.objects.all()


class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	login_url = '/login/'
	template_name = 'form.html'
	# success_url = '/restaurants/'
	
	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		return super(RestaurantCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Restaurant'
		return context