from django import forms

class ComentForm(forms.Form):
    name = forms.CharField(label="Escribi NOMBRE SAPO",max_length=30,help_text="Maximo 30")
    url = forms.URLField(label="Tu sitio puñeta",required=False,initial="http://")
    comment = forms.CharField()

class ContactForm(forms.Form):
    name = forms.CharField(label="Tu nombre Puñeta",
                           max_length=50,
                           widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Tu email puñeta",max_length=80,widget=forms.EmailInput(attrs={"class":"form-control"}))
    message = forms.CharField(label="mensagea puñeta",widget=forms.Textarea(attrs={"class":"form-control"}))

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name != "Open":
            raise forms.ValidationError("MANO NO PODES, BRUTO")
            #nonas
        else:
            #sizas
            return name
    