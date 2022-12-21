from django.urls import path
from .views import TestimonioPageView
urlpatterns = [
    #Path noticia
    path('', TestimonioPageView.as_view(), name='home'),
]
