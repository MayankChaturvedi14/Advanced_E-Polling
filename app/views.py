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
            return render(request,'join.html')


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
    if request.method == "POST":
        bjp =request.POST.get("BJP",False)
        # print("########## INC ########\n\n\n",request.POST["INC"],"\n\n\n")
        inc =request.POST.get("INC",False)
        bsp =request.POST.get("BSP",False)
        tmc =request.POST.get("TMC",False)
        ncp =request.POST.get("NCP",False)
        npp =request.POST.get("NPP",False)
        aap =request.POST.get("AAP",False)
        jdu =request.POST.get("JDU",False)
        rjd =request.POST.get("RJD",False)
        sp =request.POST.get("SP",False)
        cpi =request.POST.get("CPI",False)
        cpim =request.POST.get("CPIM",False)
        rld =request.POST.get("RLD",False)
        nota =request.POST.get("NOTA",False)
        record = Party(BJP=bjp,INC=inc,BSP=bsp,TMC=tmc,NCP=ncp,NPP=npp,AAP=aap,JDU=jdu,RJD=rjd,SP=sp,CPI=cpi,CPIM=cpim,RLD=rld,NOTA=nota) 
        record.save()     
        return render(request,'home.html',)
    return render(request,'main.html',{"view":Cn_record})

