from django.urls import path
from home import views
from .views import landingView

urlpatterns=[
    path('',views.landingView, name='landing_page')
]