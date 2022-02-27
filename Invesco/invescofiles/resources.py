from dataclasses import fields
from pyexpat import model
from import_export import resources
from .models import *


class ClaimResource(resources.ModelResource):
    class Meta:
        model=ClaimsDataInsuredRecords
        exclude = ("date_loss","date_received")
        widgets={
            "date_loss":{"format":"%d/%m/%Y"},
            "date_received":{"format":"%d/%m/%Y"},
            "last_modified":{"format":"%d/%m/%Y"},
        }

