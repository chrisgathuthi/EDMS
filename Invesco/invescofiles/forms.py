from dataclasses import field
from logging import PlaceHolder
from msilib.schema import Extension
from django import forms
from django.forms import ClearableFileInput, DateInput, TextInput
from .models import *

#This is the model form and admin form for the hearing 
#it is meant to create the inline forms and model forms
class WarrantForms(forms.ModelForm):
    class Meta:
        model = Warrants
        exclude=["total_amount"]
class WarrantAdminForms(forms.ModelForm):
    class Meta:
        model = Warrants
        exclude=["total_amount"]


#This is the model form and admin form for the hearing 
#it is meant to create the inline forms and model forms
class HearingForms(forms.ModelForm):
    class Meta:
        model = Hearing
        fields = "__all__"
class HearingAdminForms(forms.ModelForm):
    class Meta:
        model = Hearing
        fields = "__all__"


#This is the model form and admin form for the Judgment
#it is meant to create the inline forms and model forms
class JudgementForms(forms.ModelForm):
    class Meta:
        model = Judgement
        fields = "__all__"

class JudgementAdminForms(forms.ModelForm):
    class Meta:
        model = Judgement
        fields = "__all__"

#This is the model form and admin form for the OutOfCourt
#it is meant to create the inline forms and model forms  
class OutOfCourtForms(forms.ModelForm):
    class Meta:
        model = OutOfCourt
        exclude=["outs_balance"]
        widgets = {
            'medical_rep': forms.ClearableFileInput(attrs={'multiple': True}),        
        }
class OutOfCourtAdminForms(forms.ModelForm):
    class Meta:
        model = OutOfCourt
        exclude=["outs_balance"]
        widgets = {
            'medical_rep': forms.ClearableFileInput(attrs={'multiple': True}),        
        }
#This is the model form and admin form for the StaturoryNotice
#it is meant to create the inline forms and model forms   
class StatutoryNoticeForms(forms.ModelForm):
    claim_no = forms.ModelChoiceField(queryset=StatutoryNotice.objects.all(), empty_label='Select the claim No')
    class Meta:
        model = StatutoryNotice
        fields = "__all__"
        widgets = {
            'date_received': forms.DateInput(format=('%d-%m-%Y'),attrs={'placeholder': 'select a date  e.g. dd/mm/YYY'}),
        }
class StaturoryNoticeAdminForms(forms.ModelForm):
    class Meta:
        model = StatutoryNotice
        fields = "__all__"

#This is the model form and admin form for the satutroty notices
#it is meant to create the inline forms and model forms   
class SummonForms(forms.ModelForm):
    class Meta:
        model = Summon
        fields = "__all__"
class SummonAdminForms(forms.ModelForm):
    class Meta:
        model = Summon
        fields = "__all__"

#This is the claims Records of the insured.
class ClaimsDataInsuredRecordsForms(forms.ModelForm):
    class Meta:
        model = ClaimsDataInsuredRecords
        fields = "__all__"
        
"""
    The class is used to override the Admin fileiput widget to allow multiple file input, the class is also defined
    in the admin.py fil and the class name is used as the form variable

"""
class ClaimsRecordFilesForm(forms.ModelForm):
    class Meta:
        model = ClaimRecordsFiles
        fields = "__all__"
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True}),
        }


class ClaimsRecordFilesAdminForms(forms.ModelForm):
    class Meta:
        model = ClaimRecordsFiles
        fields = "__all__"
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True}),
        }
        




"""
#we might need this to make the foreignkey widget
from django.forms import TextInput
from django.db import models

class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete':'off', 'class':'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete':'off', 'class':'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete':'off', 'class':'vURLField'})},
    }"""
