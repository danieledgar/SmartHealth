from django.shortcuts import render
from django.views.generic import TemplateView
from .models import data

# Create your views here.

def landingView(request):
    return render(request,'home/landing.html')

class home(TemplateView):
    model=data
    template_name='home/home.html'
    fields=['temperature','steps_walked','heartbeat']

    def form_valid(self,form):
        form.instance.author=self.request_user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        
        return context
