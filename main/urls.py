from django.urls import path
from . import views
from .views import BeneficiarioCreateView, BeneficiarioUpdateView

urlpatterns = [
    path('', views.Beneficiarioview, name='beneficiario-lista'),
    
    path('beneficiariosID/<int:id>', views.BeneficiarioIDview, name='beneficiario-detalhe'),

    path('contact', views.contact_view, name='beneficiario-contact'),

    path('beneficiario/create/', BeneficiarioCreateView.as_view(), name='beneficiario-create'),

    path('beneficiario/<int:pk>/update/', views.BeneficiarioUpdateView.as_view(), name='beneficiario-update'),
]