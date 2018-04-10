import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		num = random.randint(0, 10000)

		context = {
			'num': num,
		}

		return context		

class AboutView(TemplateView):
	template_name = 'about.html'

	def get_context_data(self, *args, **kwargs):
		context = super(AboutView, self).get_context_data(*args, **kwargs)
		
		return context		

class ContactView(TemplateView):
	template_name = 'contact.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ContactView, self).get_context_data(*args, **kwargs)
		
		return context		