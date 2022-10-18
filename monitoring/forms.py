from django import forms


class AsinForm(forms.Form):
    asin = forms.CharField(
        label="Asin",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control m-1"}),
    )
