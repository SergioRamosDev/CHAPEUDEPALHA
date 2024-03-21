from django.shortcuts import render
from .models import Beneficiario
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from django.views.generic import CreateView
from django.views.generic import UpdateView

class BeneficiarioCreateView(CreateView):
    model = Beneficiario
    fields = '__all__'  # Ou especifique os campos que deseja incluir no formulário

class BeneficiarioUpdateView(UpdateView):
    model = Beneficiario
    fields = '__all__'


def Beneficiarioview(request):
    Beneficiario_list = Beneficiario.objects.all()
    return render(request, 'main/beneficiarios.html', {'beneficiario_list': Beneficiario_list})

def BeneficiarioIDview(request, id):
    Beneficiario = get_list_or_404(Beneficiario, pk=id)
    print(Beneficiario)
    return render(request, 'main/BeneficiarioID.html', {'Beneficiario':Beneficiario})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print('name:', name)
        print('email:',email)
        print('message:',message)
    return render(request, 'main/contact.html')

