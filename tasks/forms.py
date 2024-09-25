from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=99,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search..."})
    )
