from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.models import UserType
from dashboard.permissions import HasCustomerAccessPermission
# Create your views here.

class CustomerDashboardHomeView(LoginRequiredMixin,HasCustomerAccessPermission, TemplateView):
    template_name = "dashboard/customer/home.html"
