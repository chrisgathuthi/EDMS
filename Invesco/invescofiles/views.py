
import json
from django.core.files.base import File
from django.http import request
from django.shortcuts import get_list_or_404, render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core import serializers
from .models import *
from .models import ClaimsDataInsuredRecords
from .filters import *
from .forms import *
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView
from django.views.generic import *

# Create your views here.


#signIn
def Signin(request):
    if request.method == "POST":
        Username = request.POST['Username']
        Password = request.POST['Password']

        user=authenticate(request,username=Username,password=Password)
        if user is not None:
            login(request,user)
            messages.success(request,f"welcome {user}")
            return redirect("invescofiles:index")
        else:
            messages.info(request,"Invalid user")
            return redirect("invescofiles:login")
    else:
        return render(request,"login.html")


#searching through the doscs
@login_required
def index(request):
    allclaims = ClaimsDataInsuredRecords.objects.all()
    myFilters=ClaimsDataInsuredRecordsFilter(request.GET, queryset=allclaims)
    allclaims=myFilters.qs
    paginator = Paginator(allclaims, 25) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"index.html",{"allclaims":allclaims,"myFilters":myFilters,"page_obj":page_obj})

@login_required
def dashboardpage(request, id):
    allclaims = ClaimsDataInsuredRecords.objects.get(id=id)
    relatedsummons = allclaims.summon_set.all()
    relatedhearing = allclaims.hearing_set.all()
    relatedjudgement = allclaims.judgement_set.all()
    relatedoutofcourt = allclaims.outofcourt_set.all()
    relatedclaimrecordsfiles = allclaims.claimrecordsfiles_set.all()
    context={"allclaims":allclaims,"relatedsummons":relatedsummons,"relatedhearing":relatedhearing,"relatedjudgement":relatedjudgement,
    "relatedoutofcourt":relatedoutofcourt,"relatedclaimrecordsfiles":relatedclaimrecordsfiles}
    return render(request,"dashboard.html",context)


#library view
def libraryview(request):
    return render(request,"library.html")


    
#class DashboardDetailView(DetailView):
 #   """This is a dashboard class view"""
  #  model= ClaimsDataInsuredRecords
   # template_name ="test/dash_details.html"
    #queryset= ClaimsDataInsuredRecords.objects.all()
    #context_object_name = "claims"
   # def get_object(self,queryset=None):
        #id_= self.kwargs.get("id")
        #print(id_)
    
    #    return ClaimsDataInsuredRecords.objects.get(id=self.kwargs.get("id"))
        

#class ClaimsRecordsListView(ListView):
    #model = ClaimsDataInsuredRecords
    #template_name = "test/dash_details.html"
    #queryset= ClaimsDataInsuredRecords.objects.all()
    
    #context_object_name = "allclaims"
    #paginate_by = 10

    


#The summons view together with other CRUD operations
def summons_list_view(request):
    summon = Summon.objects.all()
    summonfilters= SummonsFilter(request.GET,queryset=summon )
    summon= summonfilters.qs
   # summon = claims.summons_set.all() 
    return render(request,"summon/list_summons.html",{"summon":summon,"summonfilters":summonfilters})
#summons create view
def summons_form_view(request):
    if request.method == "POST":
        form = SummonForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"form is successfully saved")
            return redirect("invescofiles:list-summons")
    else:
        form = SummonForms()
    return render(request,"summon/form_summons.html",{"form":form})

#summons update view
def summons_update_view(request,id=None):
    obj =get_object_or_404(Summon,id=id)
    form = SummonForms(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"form is successfully updated")
        return redirect("invescofiles:list-summons")
    else:
        form = SummonForms(request.POST or None,instance=obj)
    return render(request,"summon/form_summons.html",{"form":form})
#summons delete view
def summons_delete_view(request,id):
    obj =Summon.objects.get(id=id)
    obj.delete()
    return redirect("invescofiles:list-summons")


"""This it the staturory notices"""
#The staturoy view together with other CRUD operations

def statutory_list_view(request):
    statutory = StatutoryNotice.objects.all()
    statutoryfilters= StatutoryNoticeFilter(request.GET,queryset=statutory )
    statutory= statutoryfilters.qs
    return render(request,"statutory/statutory_list.html",{"statutory":statutory,"statutoryfilters":statutoryfilters})
#summons create view
def statutory_form_view(request):
    if request.method == "POST":
        form = StatutoryNoticeForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"form is successfully saved")
            return redirect("invescofiles:statutory-list")
    else:
        form = StatutoryNoticeForms()
    return render(request,"statutory/statutory_forms.html",{"form":form})

#statutory update view
def statutory_update_view(request,id=None):
    obj =get_object_or_404(StatutoryNotice,id=id)
    form = StatutoryNoticeForms(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"form is successfully updated")
        return redirect("invescofiles:list-summons")
    else:
        form = StatutoryNoticeForms(request.POST or None,instance=obj)
    return render(request,"statutory_forms.html",{"form":form})
#statutory delete view
def statutory_delete_view(request,id):
    obj =StatutoryNotice.objects.get(id=id)
    obj.delete()
    return redirect("invescofiles:statutory-list")



"""This is the logic view for all the out of court models """

def outofcourt_list_view(request):
    outofcourt = OutOfCourt.objects.all()
    outofcourtfilters= OutOFCourtFilter(request.GET,queryset=outofcourt )
    outofcourt= outofcourtfilters.qs
    return render(request,"outofcourt/outofcourt_list.html",{"outofcourt":outofcourt,"outofcourtfilters":outofcourtfilters})

#out of court create view
def outofcourt_form_view(request):
    if request.method == "POST":
        form = OutOfCourtForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"form is successfully saved")
            return redirect("invescofiles:outofcourt/outofcourt-list")
    else:
        form = OutOfCourtForms()
    return render(request,"outofcourt/outofcourt_forms.html",{"form":form})

#ourt of court update view
def outofcourt_update_view(request,id=None):
    obj =get_object_or_404(OutOfCourt,id=id)
    form = OutOfCourtForms(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"form is successfully updated")
        return redirect("invescofiles:outofcourt/outofcourt-list")
    else:
        form = OutOfCourtForms(request.POST or None,instance=obj)
    return render(request,"outofcourt/outofcourt_forms.html",{"form":form})
#out of court delete view
def outofcourt_delete_view(request,id):
    obj =OutOfCourt.objects.get(id=id)
    obj.delete()
    return redirect("invescofiles:outofcourt-list")



"""This is the logic view for all the judgements models """
def judgement_list_view(request):
    judgement = Judgement.objects.all()
    judgementfilters= JudgementFilter(request.GET,queryset=judgement )
    judgement= judgementfilters.qs
    return render(request,"judgements/list_judgement.html",{"judgement":judgement,"judgementfilters":judgementfilters})

def judgement_form_view(request):#out of court create view
    if request.method == "POST" :
        form = JudgementForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"form is successfully saved")
            return redirect("invescofiles:judgement-list")
    else:
        form = JudgementForms()
    return render(request,"judgement/form_judgements.html",{"form":form})

#ourt of court update view
def judgement_update_view(request,id=None):
    obj =get_object_or_404(Judgement,id=id)
    form = JudgementForms(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"form is successfully updated")
        return redirect("invescofiles:judgement-list")
    else:
        form = JudgementForms(request.POST or None,instance=obj)
    return render(request,"judgement/form_judgement.html",{"form":form})

def judgement_delete_view(request,id):#out of court delete view
    obj = Judgement.objects.get(id=id)
    obj.delete()
    return redirect("invescofiles:judgement-list")



"""This is the logic view for all the judgements models """
def judgement_list_view(request):
    judgement = Judgement.objects.all()
    judgementfilters= JudgementFilter(request.GET,queryset=judgement )
    judgement = judgementfilters.qs
    return render(request,"judgements/list_judgements.html",{"judgement":judgement,"judgementfilters":judgementfilters})

def judgement_form_view(request):#out of court create view
    if request.method == "POST":
        form = JudgementForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"form is successfully saved")
            return redirect("invescofiles:judgement-list")
    else:
        form = JudgementForms()
    return render(request,"judgements/form_judgements.html",{"form":form})

#ourt of court update view
def judgement_update_view(request,id=None):
    obj =get_object_or_404(Judgement,id=id)
    form = JudgementForms(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"form is successfully updated")
        return redirect("invescofiles:judgement-list")
    else:
        form = JudgementForms(request.POST or None,instance=obj)
    return render(request,"judgements/list_judgements.html",{"form":form})

def judgement_delete_view(request,id):#out of court delete view
    obj = Judgement.objects.get(id=id)
    obj.delete()
    return redirect("invescofiles:judgement-list")


"""This is the logic view for all the  models """
def hearing_list_view(request):
    hearing = Hearing.objects.all()
    hearingfilters= HearingFilter(request.GET,queryset=hearing )
    hearing= hearingfilters.qs
    return render(request,"hearings/list_hearing.html",{"hearing":hearing,"hearingfilters":hearingfilters})

def hearing_form_view(request):#out of court create view
    if request.method == "POST":
        form = HearingForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"form is successfully saved")
            return redirect("invescofiles:hearing-list")
    else:
        form = HearingForms()
    return render(request,"hearings/form_hearing.html",{"form":form})

#Hearing update view
def hearing_update_view(request,id=None):
    obj =get_object_or_404(Hearing,id=id)
    form = HearingForms(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"form is successfully updated")
        return redirect("invescofiles:hearing-list")
    else:
        form = HearingForms(request.POST or None,instance=obj)
    return render(request,"hearing/form_hearing.html",{"form":form})

def hearing_delete_view(request,id):#out of court delete view
    obj = Hearing.objects.get(id=id)
    obj.delete()
    return redirect("invescofiles:hearing-list")


"""This is the logic view for all the  models """
def warrants_list_view(request):
    warrants = Warrants.objects.all()
    warrantsfilters= WarrantsFilter(request.GET,queryset=warrants )
    warrants= warrantsfilters.qs
    return render(request,"warrants/list_warrants.html",{"warrants":warrants,"warrantsfilters":warrantsfilters})

def warrants_form_view(request):#out of court create view
    if request.method == "POST":
        form = WarrantForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"form is successfully saved")
            return redirect("invescofiles:warrant-list")
    else:
        form = HearingForms()
    return render(request,"warrants/form_warrants.html",{"form":form})

#Hearing update view
def warrants_update_view(request,id=None):
    obj =get_object_or_404(Warrants,id=id)
    form = WarrantForms(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"form is successfully updated")
        return redirect("invescofiles:warrant-list")
    else:
        form = WarrantForms(request.POST or None,instance=obj)
    return render(request,"warrants/form_warrants.html",{"form":form})

def warrants_delete_view(request,id):#out of court delete view
    obj = Warrants.objects.get(id=id)
    obj.delete()
    return redirect("invescofiles:warrants-list")

#File upload  views
def file_list_view(request):
    files = ClaimRecordsFiles.objects.all()
    filesfilters= ClaimRecordsFilesFilter(request.GET,queryset=files)
    files= filesfilters.qs
    return render(request,"uploads/list_uploads.html",{"files":files,"filesfilters":filesfilters})

def fileform(request):
    if request.method == "POST":
        form = ClaimsRecordFilesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            instance = request.FILES.getlist('file')
            claim_no=request.POST['claim_no']
            for f in instance:
                print(f)
                item1 = ClaimRecordsFiles.objects.create(
                    file=f,
                    claim_no_id=claim_no
                )   
            return redirect("invescofiles:upload-list")
    else:
        form = ClaimsRecordFilesForm(request.GET)
    return render(request,"uploads/form_uploads.html",{"form":form})


def file_update_view(request,id=None):
    obj =get_object_or_404(ClaimRecordsFiles,id=id)
    form = ClaimsRecordFilesForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"form is successfully updated")
        return redirect("invescofiles:upload-list")
    else:
        form = ClaimsRecordFilesForm(request.POST or None,instance=obj)
    return render(request,"uploads/form_uploads.html",{"form":form})

def file_delete_view(request,id):#out of court delete view
    obj = ClaimRecordsFiles.objects.get(id=id)
    obj.delete()
    return redirect("invescofiles:upload-list")



''' import csv
from datetime import datetime
from .models import *
with open(path,"r") as file:
    reader= csv.reader(file)
    for rows in reader:
        if rows ==True:
            continue
            obj = ClaimsDataInsuredRecords.objects.update_or_create(
            claim_no=str(rows[0]),
            policy_no=0,
            insured=str(rows[1]),
            plate_no=str(rows[2]),
            details_loss=str(rows[3]),
            date_loss=datetime.strptime(rows[4],"%d/%m/%Y"),
            date_received= datetime.now(),
            last_modified= datetime.now()
            )
             '''
