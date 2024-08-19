from django.shortcuts import render, redirect
from .forms import DeeplinkForm 
from djangoScrapingIds.validations import validacionInput

def webscraping(request):
    msnEstado = False
    msnError = ''
    msnResp = ''
    msnNOEXResp = ''
    msnNOVALResp = ''
    msnVal = []
    if request.method == "POST":
        form = DeeplinkForm(request.POST)
        if form.is_valid():
            msnEstado = True
            idCategoria = request.POST['idcategoria']
            tipoNavegador = request.POST['navegador']
            tipoUrl = request.POST['tipoUrl']
            msnVal = validacionInput(idCategoria,tipoNavegador,tipoUrl)
            if (len(msnVal[2]) > 1):
                if msnVal[2][1] == 'validation-field':
                    msnNOVALResp = msnVal[2][0]
            if (len(msnVal[1]) > 1):
                if msnVal[1][1] == 'no-exit-field':
                    msnNOEXResp = msnVal[1][0]
            if (len(msnVal[0]) > 1):
                if msnVal[0][1] == 'error-field':
                    msnError = msnVal[0][0]
                if msnVal[0][1] == 'exit-field':
                    msnResp = msnVal[0][0]
            redirect('/')
    else:
        form = DeeplinkForm()
	
    return render(request, 'pages/index.html',{'form':DeeplinkForm,'msnEstado':msnEstado,'msnError':msnError,'msnResp':msnResp,'msnNOEXResp':msnNOEXResp,'msnNOVALResp':msnNOVALResp})