from django import forms

class CreateForm(forms.Form):
    product_id=forms.IntegerField(
        label='Enter Product ID',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Product ID',
                'class':'form-control'
            }
        )
    )

    product_name=forms.CharField(
        label='Enter Product Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )

    product_cost=forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )

    product_color=forms.CharField(
        label='Enter Product Color',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )

    product_class=forms.CharField(
        label='Enter Product Class',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )

    customer_name=forms.CharField(
        label='Enter Customer Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Name'
            }
        )
    )

    customer_mobile=forms.IntegerField(
        label='Enter Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )

    customer_email=forms.EmailField(
        label='Enter Email ID',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email ID'
            }
        )
    )

class UpdateForm(forms.Form):
    product_id=forms.IntegerField(
        label='Enter Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )

    product_cost=forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )

class DeleteForm(forms.Form):
    product_id=forms.IntegerField(
        label='Enter Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )