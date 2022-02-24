from email.contentmanager import raw_data_manager
from django.contrib import admin
from .models import *
from .forms import *
from invescofiles.models import *
from import_export import resources

#{ClaimRecordsFiles, ClaimsDataInsuredRecords,ClaimPlaintiffRecords,
#Summon,StaturoryNotice,Judgment,Warrants,Ira,OutOfCourt}
# Register your models here.

#admin.site.register(Folder)
#admin.site.register(FolderItem)

class SummonAdmin(admin.ModelAdmin):
    list_display = ('claim_no','claimant','defendant','case_no','station','tp_adv','panel_adv','reserve_amount','instruct','remarks')
    form = SummonAdminForms
    search_fields = ['claim_no__claim_no','claimant','case_no']
    raw_id_fields=["claim_no"]
admin.site.register(Summon, SummonAdmin)

class StaturoryNoticeAdmin(admin.ModelAdmin):
    list_display = ('policy_no','plate_no','date_received','panel_adv','tp_adv','action','assign_to')
    search_fields = ['claim_no__policy_no','plate_no','date_received']
    form = StaturoryNoticeAdminForms
admin.site.register(StatutoryNotice,StaturoryNoticeAdmin)
 
class HearingAdmin(admin.ModelAdmin):
    list_display = ('claim_no','date_received','station','case_no','plaintiff','defendant','panel_adv','tp_adv','magistrate','hearing_date','bring_up_date','date_of_service','assign_to','remarks','last_modified')
    form = HearingAdminForms
    search_fields = ['claim_no__claim_no','case_no','date_received','magistrate']
    raw_id_fields=["claim_no"]
admin.site.register(Hearing,HearingAdmin)

#warrant register
class WarrantAdmin(admin.ModelAdmin):
    list_display = ('claim_no','date_received','execution_received','court_station','plaintiff','defendant','court_station','tp_adv','auctioneer','warrant_amount','auctioneer_amount','total_amount','assign_to')
    form = WarrantAdminForms
    search_fields = ['claim_no__claim_no','date_received','execution_received','magistrate']
    raw_id_fields=["claim_no"]
admin.site.register(Warrants,WarrantAdmin)

#judgment admin forms
class JudgementAdmin(admin.ModelAdmin):
    list_display = ('claim_no','date_received','case_no','insured','claimant','station','pri_decl')
    form = JudgementAdminForms
    raw_id_fields=["claim_no"]
    search_fields = ['claim_no__claim_no','date_received','case_no','insured']
admin.site.register(Judgement,JudgementAdmin)


#out of court Admin
class OutOfCourtAdmin(admin.ModelAdmin):
    list_display = ('claim_no','complaint','negotiated','amount_approved','amount_paid','outs_balance')
    form = OutOfCourtAdminForms
    raw_id_fields=["claim_no"]
    search_fields = ['claim_no__claim_no','negotiated']
admin.site.register(OutOfCourt,OutOfCourtAdmin)


"""
    The two classes below are for creating stackedinline model
    the form =ClaimsDataInsuredRecordsAdminForm
    is a form created in the forms.py and it has some widgets that we have
    overriden in the admin page

"""
#class ClaimPlaintiffRecordsInline(admin.StackedInline):
 #   model=ClaimPlaintiffRecords
  #  extra = 0
class ClaimsDataInsuredRecordsAdmin(admin.ModelAdmin):     
    list_filter = ('date_received',) 
    list_display = ['claim_no','policy_no','insured','plate_no','details_loss','date_received','last_modified']
    search_fields = ['claim_no','policy_no','insured','plate_no']
admin.site.register(ClaimsDataInsuredRecords,ClaimsDataInsuredRecordsAdmin)

"""
    we are overriding the dropdown for searching through plaintiffs models
"""
class ClaimRecordsFilesAdmin(admin.ModelAdmin):
    raw_id_fields=["claim_no"]
    form = ClaimsRecordFilesAdminForms
    list_display = ['claim_no','file','title','description','date_of_submission','last_modified']
    search_fields = ['claim_no__claim_no','title']
admin.site.register(ClaimRecordsFiles,ClaimRecordsFilesAdmin)


#django import export module

class ClaimsResource(resources.ModelResource):
    class Meta:
        model = ClaimsDataInsuredRecords