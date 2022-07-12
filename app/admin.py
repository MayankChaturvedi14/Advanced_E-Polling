from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Registeration,Cn_Registeration,Party

# Register your models here.
@admin.register(Registeration)
class SudoRegistration(admin.ModelAdmin):
    list_display = ['Name','Email','Mobile','Address','Aadhar','VoterID',"DOB"]
    
@admin.register(Cn_Registeration)
class SudoCn_Registeration(admin.ModelAdmin):
    list_display = ['Candidate_Name','Party','Mobile','Gender','doc_file']

@admin.register(Party)
class SudoParty(admin.ModelAdmin):
    list_display = ['BJP','INC','BSP','TMC','NCP','NPP','AAP','JDU','RJD','SP','CPI','CPIM','RLD','NOTA']

# @admin.register(User)
# class SudoUser(admin.ModelAdmin):
#     list_display = ["user_name","VoterID","DOB"]