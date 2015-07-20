from django import forms

class NowaFirmaForm(forms.Form):
    nazwa = forms.CharField(label='Nazwa firmy', max_length=60)
    wlasciciel_imie = forms.CharField(label='Imię właściciela',
                                      max_length=30)
    wlasciciel_nazwisko = forms.CharField(label='Nazwisko właściciela', max_length=30)
    def clean(self):
        cleaned_data = super(NowaFirmaForm, self).clean()
        nazwa = cleaned_data.get("nazwa")
        wlasciciel = cleaned_data.get("wlasciciel_imie") or cleaned_data.get("wlasciciel_nazwisko")
        if not (nazwa or wlasciciel):
            raise forms.ValidationError("Co najmniej jedno z pól Nazwa i Właściciel musi "
                                        "być wypełnione")
