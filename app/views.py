from django.shortcuts import render
from django.contrib.auth import login
from django.contrib import messages
from .models import MyUser, Registeration,Cn_Registeration,Party

def index(request):
    return render(request,'home.html')

def join(request):
    if request.method=="POST":
        if request.POST.get("login")=="Login":
            username = request.POST["user_name"]
            vid = request.POST["vid"]
            dob = request.POST["dob"]
            if("/" in dob):
                year = dob.split("/")[-1]
                month = dob.split("/")[-2]
                day = dob.split("/")[-3]
                dob = f"{year}-{month}-{day}"
            user_data = MyUser.objects.filter(user_name=username,VoterID=vid,DOB=dob)
            try:
                login(request,user_data[0])
                return render(request,'main.html')
            except:
                messages.info(request, 'Username/Voter ID/DOB may be incorrect, Please Try Again.')
                return render(request,"join.html")

        if request.POST.get("signup")=="Signup":
            username = request.POST["user_name"]
            email = request.POST["email"]
            address = request.POST["address"]
            phone = request.POST["pno"]
            aadhar = request.POST["aadhar"]
            vid = request.POST["voterid"]
            dob = request.POST["dob"]
            dob = dob.split("/")
            formatted_date = dob[2]+"-"+dob[1]+"-"+dob[0]
            # print(f"\n\n\n\n=======>  {formatted_date}  <===========\n\n\n\n")
            record = Registeration(Name=username,Email=email,Mobile=phone,Address=address,Aadhar=aadhar,VoterID=vid,DOB=formatted_date) 
            record.save()
            user_record = MyUser(user_name = username, VoterID=vid, DOB=formatted_date)          
            user_record.save()
            return render(request,'home.html')

    return render(request,'join.html')

def faq(request):
    return render(request,'faq.html')

def about(request):
    return render(request,'about.html')

def ad(request):
    return render(request,'admin.html')

def list(request):
    return render(request,'list.html')

def result(request):
    return render(request,'result.html')


def cn(request):
    if request.method == "POST":
        candidatename = request.POST["cname"]
        Partyfor = request.POST["party"]
        phone = request.POST["phone"]
        gender = request.POST["Gender"]
        choice = request.POST.get("case")
        if(choice.lower()=="yes"):
            doc_file=request.FILES.get("docfile")  
            record = Cn_Registeration(Candidate_Name=candidatename,Party=Partyfor,Mobile=phone,Gender=gender,doc_file=doc_file) 
            record.save()   
        else:
            record = Cn_Registeration(Candidate_Name=candidatename,Party=Partyfor,Mobile=phone,Gender=gender) 
            record.save()   
        return render(request,'admin.html')
    return render(request,'cn.html')

def main(request):
    Cn_record = Cn_Registeration.objects.all()
    record = Party.objects.filter(id=1)
    if not record:
        record = Party(id=1)
        record.save()

    if request.method == "POST":
        bjp =int(request.POST.get("BJP",0) and 1)
        # print("########## INC ########\n\n\n",request.POST["INC"],"\n\n\n")
        inc =int(request.POST.get("INC",0) and 1)
        bsp =int(request.POST.get("BSP",0) and 1)
        tmc =int(request.POST.get("TMC",0) and 1)
        ncp =int(request.POST.get("NCP",0) and 1)
        npp =int(request.POST.get("NPP",0) and 1)
        aap =int(request.POST.get("AAP",0) and 1)
        jdu =int(request.POST.get("JDU",0) and 1)
        rjd =int(request.POST.get("RJD",0) and 1)
        sp =int(request.POST.get("SP",0) and 1)
        cpi =int(request.POST.get("CPI",0) and 1)
        cpim =int(request.POST.get("CPIM",0) and 1)
        rld =int(request.POST.get("RLD",0) and 1)
        nota =int(request.POST.get("NOTA",0) and 1)
        Party.objects.filter(id=1).update(BJP=record[0].BJP+bjp, INC=record[0].INC+inc, BSP=record[0].BSP+bsp, TMC=record[0].TMC+tmc, NCP=record[0].NCP+ncp, NPP=record[0].NPP+npp, AAP=record[0].AAP+aap, JDU=record[0].JDU+jdu, RJD=record[0].RJD+rjd, SP=record[0].SP+sp, CPI=record[0].CPI+cpi, CPIM=record[0].CPIM+cpim, RLD=record[0].RLD+rld, NOTA=record[0].NOTA+nota)
        return render(request,'home.html',)
    return render(request,'main.html',{"view":Cn_record})

