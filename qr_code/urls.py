from django.urls import path
from . import views

urlpatterns = [
    # other patterns...
    path('generate-qr-code', views.generate_qr_code, name='generate_qr_code'),
    path('gaming',views.gaming,name='gaming'),
]