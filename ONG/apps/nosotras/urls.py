from django.urls import path
from .views import *

urlpatterns = [
    path('', NosotrasPageView.as_view(), name='nosotras'),
]
