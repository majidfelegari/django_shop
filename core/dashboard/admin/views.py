from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from accounts.models import UserType
from dashboard.permissions import HasAdminAccessPermission

# Create your views here.

class AdminDashboardHomeView(LoginRequiredMixin,HasAdminAccessPermission, TemplateView):
    template_name = "dashboard/admin/home.html"
