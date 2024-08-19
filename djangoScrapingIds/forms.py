from django import forms
	
class DeeplinkForm(forms.Form):
    #idcategoria = forms.CharField()
    Choice_value = [('api','API'),('deeplink','DEEPLINK'),('excel','EXCEL')]
    tipoUrl = forms.ChoiceField(label='', choices=Choice_value, widget=forms.Select(attrs={'class':'form-control form-control-lg text-center'}))
    idcategoria = forms.CharField(label='',required=False, widget=forms.TextInput
                                  (attrs=
                                        {'class': "form-control form-control-lg",
                                        'placeholder': "Ingresar el ID o lista de IDs"}))