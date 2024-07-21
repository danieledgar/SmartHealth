from django.urls import path
from home import views
from .views import landingView, home

urlpatterns=[
    path('',views.landingView, name='landing_page'),
    path('home/',home.as_view(), name='home'),
]