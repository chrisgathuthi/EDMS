from pyexpat import model
from import_export import resources
from .models import *


class ClaimResource(resources.ModelResource):
    class Meta:
        model=ClaimsDataInsuredRecords
        fields = ("claim_no","insured","plate_no","details_loss","date_loss")

