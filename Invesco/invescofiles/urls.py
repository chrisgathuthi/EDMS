from django.urls import path
from invescofiles import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "invescofiles"
urlpatterns=[

     #The summons path
   path("list-summons/",views.summons_list_view,name="list-summons"),
   path("forms-summons/",views.summons_form_view,name="forms-summons"),#create summons
   path("update-summons/<int:id>/",views.summons_update_view,name="update-summons"),#get and post summons
   path("delete-summons/<int:id>/",views.summons_delete_view,name="delete-summons"),#delete summons

   path("",views.Signin,name="login"),#the first page for login

     #index and dashboard
   path("search/",views.index,name="index"),
   path("dashboard/<int:id>/",views.dashboardpage,name="dashboard"),
   path("library/",views.libraryview,name="library"),


   #statutory
   path("statutory-forms/",views.statutory_form_view,name="statutory-forms"),#create statutory
   path("statutory-list/",views.statutory_list_view,name="statutory-list"),#list all statutoy 
   path("update-statutory/<int:id>/",views.statutory_update_view,name="update-statutory"),#get and post statutory
   path("delete-statutory/<int:id>/",views.statutory_delete_view,name="delete-statutory"),#delete statutory

      #out of court
   path("outofcourt_forms/",views.outofcourt_form_view,name="outofcourt-forms"),#create outofcourt
   path("outofcourt-list/",views.outofcourt_list_view,name="outofcourt-list"),#list all outofcourt
   path("update-outofcourt/<int:id>/",views.outofcourt_update_view,name="update-outofcourt"),#get and post outofcourt
   path("delete-outofcourt/<int:id>/",views.outofcourt_delete_view,name="delete-outofcourt"),#delete outofcourt
      
       #hearing
   path("hearing-forms/",views.hearing_form_view,name="hearing-forms"),#create hearing
   path("hearing-list/",views.hearing_list_view,name="hearing-list"),#list all hearing
   path("update-hearing/<int:id>/",views.hearing_update_view,name="update-hearing"),#get and post hearing
   path("delete-hearing/<int:id>/",views.hearing_delete_view,name="delete-hearing"),#delete hearing


           #judgements
   path("judgement-forms/",views.judgement_form_view,name="judgment-forms"),#create hearing
   path("judgement-list/",views.judgement_list_view,name="judgement-list"),#list all hearing
   path("update-judgement/<int:id>/",views.judgement_update_view,name="update-judgement"),#get and post hearing
   path("delete-judgement/<int:id>/",views.judgement_delete_view,name="delete-judgement"),#delete hearing



               #warrants
   path("warrant-forms/",views.warrants_form_view,name="warrant-forms"),#create hearing
   path("warrant-list/",views.warrants_list_view,name="warrant-list"),#list all hearing
   path("update-warrant/<int:id>/",views.warrants_update_view,name="update-warrant"),#get and post hearing
   path("delete-warrant/<int:id>/",views.warrants_delete_view,name="delete-warrant"),#delete hearing

   #file upload
   path("upload-forms/",views.fileform,name="upload-forms"),#create hearing
   path("upload-list/",views.file_list_view,name="upload-list"),#list all hearing
   path("update-upload/<int:id>/",views.file_update_view,name="update-upload"),#get and post hearing
   path("delete-upload/<int:id>/",views.file_delete_view,name="delete-upload"),#delete hearing
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)