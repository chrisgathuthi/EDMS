
from dataclasses import fields
from tkinter import Widget
from django import forms

from django.http import QueryDict
from .models import *
import django_filters


#filters for the claims records
class ClaimsDataInsuredRecordsFilter(django_filters.FilterSet):
    class Meta:
        model=ClaimsDataInsuredRecords
        exclude =("date_received",)


#summons filter class        
class SummonsFilter(django_filters.FilterSet):
    class Meta:
        model=Summon
        exclude = ("remarks","reserve_amount","instruct")

#statutory notice filter
class StatutoryNoticeFilter(django_filters.FilterSet):
    class Meta:
        model=StatutoryNotice
        fields = "__all__"

#The views for the out of court files
class OutOFCourtFilter(django_filters.FilterSet):
    class Meta:
        model=OutOfCourt
        exclude=("medical_rep")

#The filter for the hearing model
class HearingFilter(django_filters.FilterSet):
    class Meta:
        model=Hearing
        fields = "__all__"

#The filter for the hearing model
class JudgementFilter(django_filters.FilterSet):
    class Meta:
        model= Judgement
        fields = "__all__"


#The filter for Warrants
class WarrantsFilter(django_filters.FilterSet):
    class Meta:
        model= Warrants
        fields = "__all__"


class ClaimRecordsFilesFilter(django_filters.FilterSet):
    class Meta:
        model= ClaimRecordsFiles
        exclude =  ("file",)