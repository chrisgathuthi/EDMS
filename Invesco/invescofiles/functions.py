import csv
from datetime import datetime
from .models import ClaimsDataInsuredRecords
path = r"C:\Users\HP\Documents\Dev\project\Invesco\static\data\test2.csv"
with open(path,"r",encoding="UTF8") as file:
    reader= csv.reader(file)
    for rows in reader:
        obj = ClaimsDataInsuredRecords.objects.update_or_create(
            claim_no=str(rows[1]),
            policy_no=0,
            insured=str(rows[3]),
            plate_no=str(rows[4]),
            details_loss=str(rows[5]),
            date_loss=datetime.strptime(rows[6],"%d/%m/%Y")
            )
        print(f"complete {obj.claim_no} {obj.policy_no}")
