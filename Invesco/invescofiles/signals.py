from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
''' 
@receiver(post_save,sender=ClaimsDataInsuredRecords)
def create_fileinstance(sender,instance,created,**kwargs):
    if created:
        ClaimRecordsFiles.objects.create(claim_no=instance) '''
'''         
@receiver(post_save,sender=ClaimsDataInsuredRecords)
def create_folder_instance(sender,instance,created,**kwargs):
    if created:
        Folder.objects.create(claim_no=instance) '''
        
    