from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SubmitReviewForm
from .models import ReviewModel
from django.contrib import messages

class SubmitReviewView(LoginRequiredMixin, CreateView):
    http_method_names = ["post"]
    model = ReviewModel
    form_class = SubmitReviewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        product = form.cleaned_data['product']
        messages.success(self.request, "دیدگاه شما با موفقیت ثبت شد و پس از بررسی نمایش داده خواهد شد.")
        return redirect(reverse_lazy('shop:product-detail', kwargs={"slug":product.slug}))
    
    def form_invalid(self, form):
        for feild, erros in form.errors.items():
            for error in erros:
                messages.error(self.request, error)
        
        return redirect(self.request.META.get('HTTP_REFERER'))
    
    def get_queryset(self):
        return ReviewModel.objects.filter(user=self.request.user)

# Create your views here.
