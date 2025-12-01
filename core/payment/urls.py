from django.urls import path, re_path
from . import views

urlpatterns = [
    path("verify/", views.PayementVerifyView.as_view(), name="verify")
]
