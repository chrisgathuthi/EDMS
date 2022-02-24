import csv
from datetime import datetime
from .models import ClaimsDataInsuredRecords
path = r"C:\Users\HP\Documents\Dev\project\Invesco\static\data\test2.csv"
with open(path,"r") as file:
    reader= csv.reader(file)
    for rows in reader:
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
        print(f"complete {obj.claim_no} {obj.policy_no}")
