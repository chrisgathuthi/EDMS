
from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse

# Create your models here.
class ClaimsDataInsuredRecords(models.Model):
    claim_no = models.CharField(verbose_name="claim number",max_length=25,unique=True,null=False,blank=False)
    insured = models.CharField(verbose_name="insured",max_length=100,help_text="Name of the insured",null=True,blank=True)
    plate_no = models.CharField(verbose_name="no plate",max_length=8,help_text="motor vehicle registration",null=True,blank=True)
    details_loss = models.TextField(verbose_name="details of loss",max_length=200,help_text="Details of loss",null=True,blank=True)
    date_loss = models.DateField(verbose_name="date of loss",help_text="Date of the loss",null=True,blank=True)
    date_received = models.DateField(verbose_name="date received",help_text="date received ",null=True,blank=True)
    
    
    
    def get_absolute_url(self):
        return reverse('invescofiles:dashboard', kwargs={"id":self.id})

    def __str__(self):
        return f"{self.claim_no}"

    class Meta:
        ordering = ["-claim_no"]
        verbose_name = "INSURED RECORD"
    
class Summon(models.Model):
    CLAIM=[
        ("TPPD", "TPPD"),
        ("TPP1", "TPP1"),
        ("OD", "OD"),
        ("WS", "WS"),
    ]
    claim_no= models.ForeignKey(ClaimsDataInsuredRecords,verbose_name="claim number",on_delete=models.CASCADE)
    claimant = models.CharField(verbose_name="plaintiff",max_length=100,help_text="plaintif Name",null=True,blank=True)
    defendant = models.CharField(verbose_name="defendant",max_length=100,help_text="defendant Name",null=True,blank=True)
    injury = models.CharField(verbose_name="nature of injury",choices=CLAIM,max_length=6,help_text="Nature of Injury",null=True,blank=True)
    case_no = models.CharField(verbose_name="case no",max_length=25,help_text="case number",null=True,blank=True,unique=True)
    station = models.CharField(verbose_name="court station",max_length=30,help_text="branches",null=True,blank=True)
    tp_adv = models.CharField(verbose_name="T.P advocate",max_length=30,help_text="third party advocate",null=True,blank=True)
    panel_adv = models.CharField(verbose_name="panel advocate",max_length=30,help_text="panel advocate i.e. invesco Ltd advocate",null=True,blank=True)
    reserve_amount = models.PositiveBigIntegerField(verbose_name="reserve amount",help_text="Reserve amount")
    instruct = models.CharField(verbose_name="instructed",max_length=50,help_text="Instructed",blank=True, null=True)
    remarks = models.CharField(verbose_name="remarks",max_length=50,help_text="Remarks")
    date_received = models.DateField(verbose_name="date received",help_text="date received ",null=True,blank=True,auto_created=True,auto_now=True)
    def __str__(self):
        return f"{self.claim_no}"

    

    class Meta:
        verbose_name = "SUMMON RECORD"
        ordering = ["-claim_no"]

class StatutoryNotice(models.Model):
    policy_no = models.CharField(verbose_name="policy number",max_length=25,unique=True,null=False,blank=False)
    plate_no = models.CharField(verbose_name="no plate",max_length=8,help_text="motor vehicle registration",null=True,blank=True)
    date_received = models.DateField(verbose_name="date received",help_text="date received ",null=True,blank=True,auto_created=True,auto_now=True)
    claimant = models.CharField(verbose_name="plaintiff",max_length=100,help_text="plaintif Name",null=True,blank=True)
    defendant = models.CharField(verbose_name="defendant",max_length=100,help_text="defendant Name",null=True,blank=True)
    panel_adv = models.CharField(verbose_name="panel advocate",max_length=50,help_text="panel advocate",null=True,blank=True)
    tp_adv = models.CharField(verbose_name="T.P advocate",max_length=50,help_text="third party advocate",null=True,blank=True)
    action = models.CharField(verbose_name="action",max_length=30,help_text="Action",null=True,blank=True)
    assign_to = models.CharField(verbose_name="assing to",max_length=30,help_text="Assign to")
    date_received = models.DateField(verbose_name="date received",help_text="date received ",null=True,blank=True,auto_created=True,auto_now=True)

    def __str__(self):
        return f"{self.policy_no}"

    class Meta:
        verbose_name = "STATUTORY NOTICE RECORD"
        ordering = ["-date_received"]

class Hearing(models.Model):
    date_received = models.DateField(verbose_name="date received",help_text="date received ",null=True,blank=True,auto_created=True,auto_now=True)
    claim_no= models.ForeignKey(ClaimsDataInsuredRecords,verbose_name="claim number",on_delete=models.CASCADE)
    station = models.CharField(verbose_name="court station",max_length=30,help_text="court station",null=True,blank=True)
    case_no = models.CharField(verbose_name="case no",max_length=25,help_text="case number",null=True,blank=True,unique=True)
    plaintiff = models.CharField(verbose_name="plaintiff",max_length=100,help_text="plaintif Name",null=True,blank=True)
    defendant = models.CharField(verbose_name="defendant",max_length=100,help_text="defendant Name",null=True,blank=True)
    panel_adv = models.CharField(verbose_name="panel advocate",max_length=30,help_text="panel advocate i.e. invesco Ltd advocate",null=True,blank=True)
    tp_adv = models.CharField(verbose_name="T.P advocate",max_length=50,help_text="third party advocate",null=True,blank=True)
    magistrate = models.CharField(verbose_name="magistrate's name",max_length=100,help_text="defendant Name",null=True,blank=True)
    hearing_date = models.DateField(verbose_name="hearing date",help_text="date received ",null=True,blank=True)
    bring_up_date = models.DateField(verbose_name="bring up date",help_text="hearing up date")
    date_of_service = models.DateField(verbose_name="date of service",help_text="date of service")
    assign_to = models.CharField(verbose_name="assigned to",max_length=100,help_text="defendant Name",null=True,blank=True)
    date_received = models.DateField(verbose_name="date received",help_text="date received ",null=True,blank=True,auto_created=True,auto_now=True)
    last_modified = models.DateTimeField(verbose_name="Last modified",auto_now=True,help_text="This is the date of last modification",null=True,blank=True)
    remarks = models.CharField(verbose_name="remarks",help_text="remarks",null=True,blank=True,max_length=50)
    def __str__(self):
        return f"{self.claim_no}"

    class Meta:
        verbose_name = "HEARING RECORD"
        ordering = ["-date_received"]
        
class Judgement(models.Model):
    PRI_DECL = [
        ("PRI", "PRI"),
        ("DECL", "DECL"),
    ]
    date_received = models.DateField(verbose_name="DATE RECEIVED",help_text="date received ",null=True,blank=True,auto_created=True,auto_now=True)
    claim_no= models.ForeignKey(ClaimsDataInsuredRecords,verbose_name="claim number",on_delete=models.CASCADE)
    case_no = models.CharField(verbose_name="CASE NO",max_length=25,help_text="case number",null=True,blank=True)
    insured = models.CharField(verbose_name="DEFENDANT",max_length=100,help_text="insured Name",null=True,blank=True)
    claimant = models.CharField(verbose_name="PLAINTIFF",max_length=100,help_text="Claimant Name",null=True,blank=True)
    station = models.CharField(verbose_name="COURT STATION",max_length=30,help_text="branches",null=True,blank=True)
    pri_decl= models.CharField(verbose_name="PRI/DECL",max_length=5,choices=PRI_DECL,help_text="primary/declaratory",null=True,blank=True)
    total_amount = models.PositiveBigIntegerField(verbose_name="AWARD AMOUNT",help_text="Total amount",blank=False,null=True)
    
    def __str__(self):
        return f"{self.claim_no}    |   {self.date_received}"

    class Meta:
        verbose_name = "JUDGMENT RECORD"
        ordering = ["-date_received"]

class Warrants(models.Model):
    claim_no= models.ForeignKey(ClaimsDataInsuredRecords,verbose_name="claim number",on_delete=models.CASCADE)
    date_received = models.DateField(verbose_name="date received",help_text="date received ",null=True,blank=True,auto_created=True,auto_now=True)
    execution_received = models.DateField(verbose_name="proclamation date",help_text="date received ",null=True,blank=True)
    region = models.CharField(verbose_name="branches",max_length=30,help_text="Invesco branches",null=True,blank=True)
    plaintiff = models.CharField(verbose_name="plaintiff",max_length=100,help_text="Plaintiff Name",null=True,blank=True)
    defendant = models.CharField(verbose_name="defendant",max_length=100,help_text="defendant name",null=True,blank=True)
    court_station = models.CharField(verbose_name="court station",max_length=30,help_text="court station",null=True,blank=True)
    tp_adv = models.CharField(verbose_name="T.P advocate",max_length=30,help_text="third party advocate",null=True,blank=True)
    panel_adv = models.CharField(verbose_name="panel advocate",max_length=30,help_text="third party advocate",null=True,blank=True)
    auctioneer = models.CharField(verbose_name="auctioneer name",max_length=30,help_text="auctioneer name",null=True,blank=True)
    warrant_amount = models.PositiveBigIntegerField(verbose_name="warrants amount",help_text="warrant amount",blank=True,null=True)
    auctioneer_amount = models.PositiveBigIntegerField(verbose_name= "auctioneer fees",help_text="auctioneer fees",blank=True, null=True)
    total_amount = models.PositiveBigIntegerField(verbose_name="total amount",help_text="Total amount",blank=False,null=True)
    assign_to = models.CharField(verbose_name="assign to",max_length=100,help_text="Assign To",null=True,blank=True)
   
    def __str__(self):
        return f"{self.claim_no}"


    def save(self, *args, **kwargs):
        self.total_amount = self.warrant_amount+self.auctioneer_amount
        super(Warrants, self).save(*args, **kwargs) # Call the real save() method

    class Meta:
        verbose_name = "WARRANT RECORD"
        ordering = ["-date_received"]



class OutOfCourt(models.Model):
    #def fileupload(insance,filename):
     #   dirname= insance.medical_rep#.lower().replace(" ", "-")
      #  filename= filename.lower().replace(" ", "-")
       # return "Medical-Reports/{0}/{1}".format(dirname,filename)  
    CLAIM=[
        ("TPPD", "TPPD"),
        ("TPP1", "TPP1"),
        ("OD", "OD"),
        ("WS", "WS"),
    ]
    claim_no= models.ForeignKey(ClaimsDataInsuredRecords,verbose_name="claim number",on_delete=models.CASCADE)
    complaint = models.CharField(verbose_name="claimant",max_length=100,help_text="claimant/payee",null=True,blank=True)
    injury = models.CharField(verbose_name="nature of injury",choices=CLAIM,max_length=6,help_text="Nature of Injury",null=True,blank=True)
    medical_rep  = models.FileField(verbose_name="second medical report",upload_to="Medical-Reports",help_text="Medical Reports",null=True,blank=True,validators=[FileExtensionValidator( ['pdf'] )])
    tp_adv = models.CharField(verbose_name="T.P advocate",max_length=30,help_text="third party advocate",null=True,blank=True)
    panel_adv = models.CharField(verbose_name="panel advocate",max_length=30,help_text="panel advocate i.e. invesco Ltd advocate",null=True,blank=True)
    negotiated = models.CharField(verbose_name="negotiated by",max_length=100,help_text="negotiated by",null=True,blank=True)
    amount_approved = models.PositiveBigIntegerField(verbose_name="amount approved",help_text="amount approved")
    amount_paid = models.PositiveBigIntegerField(verbose_name="amount paid",help_text="amount paid")
    outs_balance = models.PositiveBigIntegerField(verbose_name="outstanding bal.",help_text="outstanding balance",blank=True)
    date_received = models.DateField(verbose_name="date received",help_text="date received ",null=True,blank=True,auto_created=True,auto_now=True)

    def save(self, *args, **kwargs):
        self.outs_balance=self.amount_approved-self.amount_paid
        super(OutOfCourt, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return f"{self.claim_no} "
    
    class Meta:
        verbose_name = "OUT OF COURT RECORD"
        ordering = ["-claim_no"]

class ClaimRecordsFiles(models.Model):
    claim_no= models.ForeignKey(ClaimsDataInsuredRecords,verbose_name="claim number",on_delete=models.CASCADE)
    file= models.FileField(verbose_name="file",upload_to="File",help_text="Upload documents",null=False,blank=True,validators=[FileExtensionValidator( ['pdf'] )])
    date_of_submission = models.DateTimeField(verbose_name="Date of creation",auto_now_add=True,help_text="this is date of sumbmission don't fill, auto.",null=True,blank=True)
    last_modified = models.DateTimeField(verbose_name="Last modified",auto_now=True,help_text="This is the date of last modification",null=True,blank=True)

    def delete(self, *args,**kwargs):
        self.file.delete()
        return super().delete(*args,**kwargs)

    def __str__(self):
        return f"{self.claim_no}"
    
    class Meta:
        verbose_name = "SCANNED FILE"
        ordering = ["-claim_no"]

#shift+alt+A

    ''' def path_and_rename(instance, filename):
        pass
        upload_to = 'photos'
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else: '''
            # set filename as random string
            #filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file


 